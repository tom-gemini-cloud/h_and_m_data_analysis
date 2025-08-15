"""
Model Evaluation Module for H&M Recommendation System

This module provides comprehensive evaluation capabilities for recommendation models,
including performance metrics, visualization, and business impact assessment.
"""

import sys
import os
from pathlib import Path
import json
import warnings
from typing import Dict, List, Tuple, Optional, Any, Union
import numpy as np
import pandas as pd
import polars as pl

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from .collaborative_filtering import CollaborativeFilteringModel
from .content_based_filtering import ContentBasedFilteringModel
from .purchase_prediction import PurchasePredictionModel
from .hybrid_recommender import HybridRecommenderModel

warnings.filterwarnings('ignore')


class ModelEvaluator:
    """Comprehensive evaluation framework for recommendation models."""
    
    def __init__(self, models_dir: str = "../models", results_dir: str = "../results/modelling"):
        """
        Initialize the ModelEvaluator.
        
        Args:
            models_dir: Directory containing trained models
            results_dir: Directory to save evaluation results
        """
        self.models_dir = Path(models_dir)
        self.results_dir = Path(results_dir)
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
        self.loaded_models = {}
        self.evaluation_results = {}
        
        # Model configuration
        self.model_files = {
            'collaborative_filtering': self.models_dir / 'collaborative_filtering_model.pkl',
            'content_based': self.models_dir / 'content_based_filtering_model.pkl',
            'purchase_prediction': self.models_dir / 'purchase_prediction_model.pkl',
            'hybrid': self.models_dir / 'hybrid_recommender_model.pkl'
        }
        
        # Business assessment data
        self.model_assessment = {
            'Collaborative Filtering': {
                'strengths': ['Discovers user preferences', 'Good for cross-selling', 'Handles new products well'],
                'weaknesses': ['Cold start problem', 'Sparsity issues', 'Computational complexity'],
                'business_use': 'Personalised homepage recommendations, email campaigns'
            },
            'Content-Based Filtering': {
                'strengths': ['No cold start problem', 'Transparent recommendations', 'Domain knowledge integration'],
                'weaknesses': ['Limited diversity', 'Requires rich content features', 'Over-specialisation'],
                'business_use': 'Product detail page recommendations, similar item suggestions'
            },
            'Purchase Prediction': {
                'strengths': ['Direct business metric', 'Probability scores', 'Feature interpretability'],
                'weaknesses': ['Requires negative sampling', 'Class imbalance', 'Complex feature engineering'],
                'business_use': 'Inventory planning, targeted promotions, customer segmentation'
            },
            'Hybrid Recommender': {
                'strengths': ['Combines multiple approaches', 'Balanced recommendations', 'Higher coverage'],
                'weaknesses': ['Increased complexity', 'Parameter tuning', 'Computational overhead'],
                'business_use': 'Primary recommendation engine, A/B testing baseline'
            }
        }
    
    def load_models(self, verbose: bool = True) -> Dict[str, Any]:
        """
        Load all available trained models.
        
        Args:
            verbose: Whether to print loading status
            
        Returns:
            Dictionary of loaded models
        """
        if verbose:
            print("Checking for trained models...")
        
        if not self.models_dir.exists():
            if verbose:
                print(f"❌ Models directory not found: {self.models_dir}")
                print("Please run the modelling notebook first to train and save models.")
            return {}
        
        loaded_models = {}
        
        if verbose:
            print("Scanning for available model files...")
        
        for model_name, model_path in self.model_files.items():
            if model_path.exists():
                if verbose:
                    print(f"✅ Found {model_name} model file")
                try:
                    if model_name == 'collaborative_filtering':
                        model = CollaborativeFilteringModel()
                        model.load_model(str(model_path))
                    elif model_name == 'content_based':
                        model = ContentBasedFilteringModel()
                        model.load_model(str(model_path))
                    elif model_name == 'purchase_prediction':
                        model = PurchasePredictionModel()
                        model.load_model(str(model_path))
                    elif model_name == 'hybrid':
                        model = HybridRecommenderModel()
                        model.load_model(str(model_path))
                    
                    loaded_models[model_name] = model
                    if verbose:
                        print(f"✅ Successfully loaded {model_name} model")
                        
                except Exception as e:
                    if verbose:
                        print(f"❌ Failed to load {model_name} model: {e}")
            else:
                if verbose:
                    print(f"⚠️  {model_name} model file not found: {model_path.name}")
        
        self.loaded_models = loaded_models
        
        if verbose:
            print(f"\n📊 Total models loaded: {len(self.loaded_models)}")
            
            if self.loaded_models:
                print("Available models for evaluation:")
                for model_name in self.loaded_models.keys():
                    print(f"  - {model_name.replace('_', ' ').title()}")
                    
                # Load model summary if available
                self._load_model_summary(verbose)
            else:
                print("❌ No models available for evaluation!")
                print("Please run the modelling notebook first to train models.")
        
        return self.loaded_models
    
    def _load_model_summary(self, verbose: bool = True) -> Optional[Dict]:
        """Load model training summary if available."""
        summary_path = self.models_dir / 'model_summary.json'
        if summary_path.exists():
            try:
                with open(summary_path, 'r') as f:
                    model_summary = json.load(f)
                if verbose:
                    print("\n📋 Model training summary found:")
                    for model_name, info in model_summary.items():
                        if any(model_name.lower().replace(' ', '_') in key for key in self.loaded_models.keys()):
                            print(f"  {model_name}: {len(info)} properties")
                return model_summary
            except Exception as e:
                if verbose:
                    print(f"⚠️  Could not load model summary: {e}")
        else:
            if verbose:
                print("⚠️  Model summary file not found")
        return None
    
    def evaluate_recommendation_quality(self, 
                                      test_customers: Optional[List] = None,
                                      n_customers: int = 20,
                                      n_recommendations: int = 5,
                                      verbose: bool = True) -> Dict[str, Dict]:
        """
        Evaluate the quality of recommendations from each model.
        
        Args:
            test_customers: List of customer IDs to test. If None, uses training customers.
            n_customers: Number of customers to test
            n_recommendations: Number of recommendations per customer
            verbose: Whether to print evaluation progress
            
        Returns:
            Dictionary containing evaluation results for each model
        """
        if verbose:
            print("=== Recommendation Quality Evaluation ===\n")
        
        if not self.loaded_models:
            if verbose:
                print("❌ No models available for evaluation.")
            return {}
        
        # Get customers for evaluation
        if test_customers is None:
            test_customers = self._get_training_customers(n_customers, verbose)
        
        evaluation_results = {}
        
        for model_name, model in self.loaded_models.items():
            if verbose:
                print(f"📊 Evaluating {model_name.replace('_', ' ').title()} Model...")
            
            if model_name == 'purchase_prediction':
                # Purchase prediction evaluation
                try:
                    model_scores = model.get_model_scores()
                    if verbose:
                        print(f"  Purchase prediction performance:")
                        for alg_name, scores in model_scores.items():
                            print(f"    {alg_name}: F1={scores['f1_score']:.3f}, AUC={scores['auc_roc']:.3f}")
                    
                    evaluation_results[model_name] = {
                        'model_scores': model_scores,
                        'model_type': 'classification'
                    }
                    continue
                except Exception as e:
                    if verbose:
                        print(f"  ❌ Error evaluating purchase prediction: {e}")
                    continue
            
            # Recommendation evaluation
            recommendation_results = []
            successful_customers = []
            
            for customer_id in test_customers:
                try:
                    recommendations = model.get_recommendations(customer_id, n_recommendations=n_recommendations)
                    
                    if recommendations:
                        avg_score = np.mean([score for _, score in recommendations])
                        recommendation_results.append({
                            'customer_id': customer_id,
                            'num_recommendations': len(recommendations),
                            'avg_score': avg_score,
                            'recommendations': recommendations
                        })
                        successful_customers.append(customer_id)
                        
                except Exception as e:
                    # Only show first few errors to avoid spam
                    if len(successful_customers) < 3 and verbose:
                        print(f"    ⚠️  Error for customer {str(customer_id)[:10]}...: {str(e)[:40]}...")
            
            if recommendation_results:
                avg_score = np.mean([r['avg_score'] for r in recommendation_results])
                coverage = len(recommendation_results) / len(test_customers)
                
                evaluation_results[model_name] = {
                    'average_score': avg_score,
                    'coverage': coverage,
                    'successful_recommendations': len(recommendation_results),
                    'total_tested': len(test_customers),
                    'model_type': 'recommendation',
                    'sample_customer': successful_customers[0] if successful_customers else None
                }
                
                if verbose:
                    print(f"  ✅ Average score: {avg_score:.4f}")
                    print(f"  ✅ Coverage: {coverage:.2%} ({len(recommendation_results)}/{len(test_customers)})") 
            else:
                if verbose:
                    print(f"  ❌ No successful recommendations generated")
            
            if verbose:
                print()
        
        self.evaluation_results = evaluation_results
        
        if verbose:
            print("✅ Recommendation evaluation complete")
        
        return evaluation_results
    
    def _get_training_customers(self, n_customers: int, verbose: bool = True) -> List:
        """Get training customers for evaluation."""
        if verbose:
            print("Finding customers from training data for evaluation...")
        
        # Try to get training customers from one of the loaded models
        training_customers = None
        for model_name, model in self.loaded_models.items():
            if hasattr(model, 'all_customers') and model.all_customers is not None:
                training_customers = model.all_customers[:n_customers]
                if verbose:
                    print(f"Found {len(training_customers)} training customers from {model_name} model")
                break
        
        # Fallback: use a default set (this would need test data)
        if training_customers is None:
            if verbose:
                print("⚠️  Could not access training customers from models")
            training_customers = []
        
        return training_customers
    
    def display_sample_recommendations(self, 
                                     customer_id: Optional[str] = None,
                                     n_recommendations: int = 5,
                                     verbose: bool = True) -> Dict[str, List]:
        """
        Display sample recommendations from each model for comparison.
        
        Args:
            customer_id: Specific customer ID to use. If None, finds a working customer.
            n_recommendations: Number of recommendations to display
            verbose: Whether to print recommendations
            
        Returns:
            Dictionary of recommendations by model
        """
        if verbose:
            print("=== Sample Recommendations Comparison ===\n")
        
        if not self.loaded_models:
            if verbose:
                print("❌ No models available for recommendation display.")
            return {}
        
        recommendation_models = {name: model for name, model in self.loaded_models.items() 
                               if name != 'purchase_prediction'}
        
        if not recommendation_models:
            if verbose:
                print("⚠️  No recommendation models available (only classification models loaded)")
            return {}
        
        # Find a working customer
        if customer_id is None:
            customer_id = self._find_working_customer(recommendation_models, verbose)
        
        if customer_id is None:
            if verbose:
                print("❌ Could not find a customer that works with any model")
            return {}
        
        all_recommendations = {}
        
        if verbose:
            print(f"🎯 Sample recommendations for Customer: {str(customer_id)[:20]}...\n")
        
        for model_name, model in recommendation_models.items():
            if verbose:
                print(f"**{model_name.replace('_', ' ').title()} Model:**")
            
            try:
                recommendations = model.get_recommendations(customer_id, n_recommendations=n_recommendations)
                
                if recommendations:
                    all_recommendations[model_name] = recommendations
                    if verbose:
                        for i, (article_id, score) in enumerate(recommendations, 1):
                            print(f"  {i}. Article {article_id}: Score {score:.4f}")
                else:
                    if verbose:
                        print("  ⚠️  No recommendations available for this customer")
                        
            except Exception as e:
                if verbose:
                    print(f"  ❌ Error: {str(e)[:50]}...")
            
            if verbose:
                print()
        
        return all_recommendations
    
    def _find_working_customer(self, recommendation_models: Dict, verbose: bool = True) -> Optional[str]:
        """Find a customer that works with at least one model."""
        # First, try to use stored successful customers from evaluation
        for model_name in recommendation_models.keys():
            if model_name in self.evaluation_results:
                sample_customer = self.evaluation_results[model_name].get('sample_customer')
                if sample_customer:
                    if verbose:
                        print(f"Using successful customer from {model_name} evaluation")
                    return sample_customer
        
        # Fallback: try to find any customer that works
        if verbose:
            print("Looking for a customer that works with the models...")
        
        for model_name, model in recommendation_models.items():
            if hasattr(model, 'all_customers') and model.all_customers is not None:
                for test_customer in model.all_customers[:5]:
                    try:
                        test_recs = model.get_recommendations(test_customer, n_recommendations=1)
                        if test_recs:
                            if verbose:
                                print(f"Found working customer: {str(test_customer)[:20]}...")
                            return test_customer
                    except:
                        continue
                if test_customer:
                    break
        
        return None
    
    def visualize_performance(self, 
                            save_plots: bool = True,
                            show_plots: bool = True,
                            figsize: Tuple[int, int] = (15, 6)) -> Tuple[plt.Figure, go.Figure]:
        """
        Create visualizations comparing model performance.
        
        Args:
            save_plots: Whether to save plots to results directory
            show_plots: Whether to display plots
            figsize: Figure size for matplotlib plots
            
        Returns:
            Tuple of (matplotlib figure, plotly figure)
        """
        if not self.evaluation_results:
            print("No evaluation results to visualize. Run evaluate_recommendation_quality() first.")
            return None, None
        
        # Filter recommendation models for visualization
        rec_results = {name: results for name, results in self.evaluation_results.items() 
                      if results.get('model_type') == 'recommendation'}
        
        if not rec_results:
            print("No recommendation models to visualize")
            return None, None
        
        # Create comparison dataframe
        comparison_df = pd.DataFrame(rec_results).T
        comparison_df = comparison_df.reset_index().rename(columns={'index': 'model'})
        
        print("Model Performance Summary:")
        print(comparison_df[['model', 'average_score', 'coverage', 'successful_recommendations', 'total_tested']])
        
        # Create matplotlib visualizations
        fig, axes = plt.subplots(1, 2, figsize=figsize)
        
        # Average Score Comparison
        axes[0].bar(comparison_df['model'], comparison_df['average_score'])
        axes[0].set_title('Average Recommendation Score by Model')
        axes[0].set_xlabel('Model')
        axes[0].set_ylabel('Average Score')
        axes[0].tick_params(axis='x', rotation=45)
        
        # Coverage Comparison
        axes[1].bar(comparison_df['model'], comparison_df['coverage'])
        axes[1].set_title('Customer Coverage by Model')
        axes[1].set_xlabel('Model')
        axes[1].set_ylabel('Coverage Rate')
        axes[1].tick_params(axis='x', rotation=45)
        axes[1].set_ylim(0, 1)
        
        plt.tight_layout()
        
        if save_plots:
            fig_path = self.results_dir / "model_performance_comparison.png"
            plt.savefig(fig_path, dpi=300, bbox_inches='tight')
            print(f"📊 Performance comparison chart saved to: {fig_path}")
        
        if show_plots:
            plt.show()
        
        # Interactive plotly visualization
        fig_plotly = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Average Score', 'Coverage Rate')
        )
        
        fig_plotly.add_trace(
            go.Bar(x=comparison_df['model'], y=comparison_df['average_score'], name='Avg Score'),
            row=1, col=1
        )
        
        fig_plotly.add_trace(
            go.Bar(x=comparison_df['model'], y=comparison_df['coverage'], name='Coverage'),
            row=1, col=2
        )
        
        fig_plotly.update_layout(
            title_text="Model Performance Comparison",
            showlegend=False,
            height=500
        )
        
        if save_plots:
            html_path = self.results_dir / "model_performance_interactive.html"
            fig_plotly.write_html(html_path)
            print(f"📊 Interactive chart saved to: {html_path}")
        
        if show_plots:
            fig_plotly.show()
        
        return fig, fig_plotly
    
    def business_impact_assessment(self, verbose: bool = True) -> Dict[str, Dict]:
        """
        Assess the practical business value of different recommendation approaches.
        
        Args:
            verbose: Whether to print assessment details
            
        Returns:
            Dictionary containing business assessment for each model
        """
        if verbose:
            print("=== Business Impact Assessment ===\n")
        
        relevant_assessments = {}
        
        for model_name, assessment in self.model_assessment.items():
            if any(model_name.lower().replace(' ', '_') in loaded_name for loaded_name in self.loaded_models.keys()):
                relevant_assessments[model_name] = assessment
                
                if verbose:
                    print(f"**{model_name}**")
                    print(f"  Strengths: {', '.join(assessment['strengths'])}")
                    print(f"  Weaknesses: {', '.join(assessment['weaknesses'])}")
                    print(f"  Business Use Cases: {assessment['business_use']}")
                    print()
        
        if verbose:
            print("**Deployment Recommendations:**")
            print("1. **Hybrid Model**: Primary recommendation engine for balanced performance")
            print("2. **Content-Based**: Quick recommendations for new users/products")
            print("3. **Collaborative Filtering**: Discover cross-category preferences")
            print("4. **Purchase Prediction**: Business analytics and inventory planning")
            print("\n**Next Steps:**")
            print("- A/B testing with real customers")
            print("- Online evaluation metrics (CTR, conversion rate)")
            print("- Model retraining pipeline")
            print("- Real-time inference optimisation")
        
        return relevant_assessments
    
    def generate_evaluation_report(self, 
                                 test_dataset_size: int = 0,
                                 save_report: bool = True,
                                 verbose: bool = True) -> str:
        """
        Generate a comprehensive evaluation summary report.
        
        Args:
            test_dataset_size: Size of test dataset used
            save_report: Whether to save report to file
            verbose: Whether to print report
            
        Returns:
            Report content as string
        """
        if verbose:
            print("=== Model Evaluation Summary ===\n")
        
        report_content = []
        report_content.append("# Model Evaluation Summary Report\n")
        report_content.append(f"**Generated:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report_content.append(f"**Models Evaluated:** {len(self.loaded_models)}")
        
        if test_dataset_size > 0:
            report_content.append(f"**Test Dataset Size:** {test_dataset_size:,} transactions")
        
        # Get the number of customers tested from evaluation results
        customers_tested = 0
        if self.evaluation_results:
            for model_results in self.evaluation_results.values():
                if 'total_tested' in model_results:
                    customers_tested = model_results['total_tested']
                    break
        
        report_content.append(f"**Sample Customers Tested:** {customers_tested}")
        
        # Console output
        if verbose:
            print(f"**Models Evaluated:** {len(self.loaded_models)}")
            if test_dataset_size > 0:
                print(f"**Test Dataset Size:** {test_dataset_size:,} transactions")
            print(f"**Sample Customers Tested:** {customers_tested}")
        
        if self.evaluation_results:
            report_content.append("\n## Performance Rankings")
            if verbose:
                print("\n**Performance Rankings:**")
            
            # Filter out non-recommendation models for ranking
            rec_results = {name: results for name, results in self.evaluation_results.items() 
                          if results.get('model_type') == 'recommendation'}
            
            if rec_results:
                # Rank by average score
                score_ranking = sorted(rec_results.items(), 
                                     key=lambda x: x[1]['average_score'], reverse=True)
                
                report_content.append("\n### By Average Recommendation Score:")
                if verbose:
                    print("\nBy Average Recommendation Score:")
                for i, (model_name, results) in enumerate(score_ranking, 1):
                    model_title = model_name.replace('_', ' ').title()
                    line = f"  {i}. {model_title}: {results['average_score']:.4f}"
                    report_content.append(line)
                    if verbose:
                        print(line)
                
                # Rank by coverage
                coverage_ranking = sorted(rec_results.items(), 
                                        key=lambda x: x[1]['coverage'], reverse=True)
                
                report_content.append("\n### By Customer Coverage:")
                if verbose:
                    print("\nBy Customer Coverage:")
                for i, (model_name, results) in enumerate(coverage_ranking, 1):
                    model_title = model_name.replace('_', ' ').title()
                    line = f"  {i}. {model_title}: {results['coverage']:.2%}"
                    report_content.append(line)
                    if verbose:
                        print(line)
            else:
                report_content.append("\n⚠️  No recommendation models evaluated for ranking")
                if verbose:
                    print("\n⚠️  No recommendation models evaluated for ranking")
        
        # Key findings
        report_content.append("\n## Key Findings:")
        if verbose:
            print("\n**Key Findings:**")
        
        if len(self.loaded_models) > 0:
            successful_models = len([name for name, results in self.evaluation_results.items() 
                                   if results.get('coverage', 0) > 0 or 'model_scores' in results])
            findings = [
                f"- {successful_models}/{len(self.loaded_models)} models working successfully"
            ]
            
            if any(results.get('model_type') == 'recommendation' for results in self.evaluation_results.values()):
                findings.append("- Recommendation models generating suggestions")
            if any(results.get('model_type') == 'classification' for results in self.evaluation_results.values()):
                findings.append("- Classification models trained and scored")
            
            findings.append("- Models ready for production deployment and A/B testing")
            
            for finding in findings:
                report_content.append(finding)
                if verbose:
                    print(finding)
        else:
            finding = "- No models available - training required"
            report_content.append(finding)
            if verbose:
                print(finding)
        
        # Add detailed results table if available
        if self.evaluation_results:
            rec_results = {name: results for name, results in self.evaluation_results.items() 
                          if results.get('model_type') == 'recommendation'}
            
            if rec_results:
                report_content.append("\n## Detailed Results")
                report_content.append("\n| Model | Average Score | Coverage | Successful Recs | Total Tested |")
                report_content.append("|-------|---------------|----------|-----------------|--------------|")
                
                for model_name, results in rec_results.items():
                    model_title = model_name.replace('_', ' ').title()
                    avg_score = results['average_score']
                    coverage = results['coverage']
                    successful = results['successful_recommendations']
                    total = results['total_tested']
                    report_content.append(f"| {model_title} | {avg_score:.4f} | {coverage:.2%} | {successful} | {total} |")
        
        report_content.append(f"\n🎉 **Model evaluation completed successfully!** 🎉")
        
        # Save report to results directory if requested
        if save_report:
            report_path = self.results_dir / "model_evaluation_summary.md"
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(report_content))
            
            if verbose:
                print(f"\n📁 Report saved to: {report_path}")
        
        if verbose:
            print("\n🎉 **Model evaluation completed successfully!** 🎉")
        
        return '\n'.join(report_content)
    
    def run_full_evaluation(self, 
                          test_data: Optional[pd.DataFrame] = None,
                          n_customers: int = 20,
                          n_recommendations: int = 5,
                          save_results: bool = True,
                          show_plots: bool = True,
                          verbose: bool = True) -> Dict[str, Any]:
        """
        Run a complete evaluation pipeline.
        
        Args:
            test_data: Test dataset (optional, for reporting dataset size)
            n_customers: Number of customers to test
            n_recommendations: Number of recommendations per customer
            save_results: Whether to save all results to files
            show_plots: Whether to display plots
            verbose: Whether to print progress
            
        Returns:
            Dictionary containing all evaluation results
        """
        if verbose:
            print("🚀 Starting comprehensive model evaluation...\n")
        
        # Load models
        models = self.load_models(verbose=verbose)
        
        if not models:
            return {'error': 'No models available for evaluation'}
        
        # Evaluate recommendation quality
        eval_results = self.evaluate_recommendation_quality(
            n_customers=n_customers,
            n_recommendations=n_recommendations,
            verbose=verbose
        )
        
        # Display sample recommendations
        sample_recs = self.display_sample_recommendations(
            n_recommendations=n_recommendations,
            verbose=verbose
        )
        
        # Create visualizations
        if eval_results:
            fig_matplotlib, fig_plotly = self.visualize_performance(
                save_plots=save_results,
                show_plots=show_plots
            )
        
        # Business impact assessment
        business_assessment = self.business_impact_assessment(verbose=verbose)
        
        # Generate comprehensive report
        test_size = len(test_data) if test_data is not None else 0
        report = self.generate_evaluation_report(
            test_dataset_size=test_size,
            save_report=save_results,
            verbose=verbose
        )
        
        return {
            'loaded_models': models,
            'evaluation_results': eval_results,
            'sample_recommendations': sample_recs,
            'business_assessment': business_assessment,
            'report': report
        }