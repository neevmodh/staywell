import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def render_contribution(contrib):
    """Render factor contribution bar chart"""
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#0F9D58', '#F4B400', '#DB4437', '#4285F4', '#AB47BC']
    bars = ax.bar(contrib.keys(), contrib.values(), color=colors)
    ax.set_ylabel("Contribution (%)", fontsize=12)
    ax.set_xlabel("Risk Factors", fontsize=12)
    ax.set_title("Factor Contribution to Burnout Risk", fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(contrib.values()) * 1.2)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

def render_correlation_matrix(df):
    """Render correlation heatmap"""
    variables = ['sleep_hours', 'study_hours', 'screen_time', 'stress_level', 'attendance', 'burnout_score']
    available_vars = [v for v in variables if v in df.columns]
    
    if len(available_vars) < 2:
        st.info("Not enough variables for correlation analysis")
        return
    
    corr = df[available_vars].corr()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdYlGn_r', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
    ax.set_title("Correlation Matrix", fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

def render_distribution(df):
    """Render distribution plots for key variables"""
    variables = ['sleep_hours', 'study_hours', 'screen_time', 'stress_level', 'attendance']
    available_vars = [v for v in variables if v in df.columns]
    
    if not available_vars:
        st.info("No variables available for distribution analysis")
        return
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    axes = axes.flatten()
    
    for idx, var in enumerate(available_vars):
        if idx < len(axes):
            axes[idx].hist(df[var], bins=15, color='#0F9D58', alpha=0.7, edgecolor='black')
            axes[idx].axvline(df[var].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df[var].mean():.1f}')
            axes[idx].axvline(df[var].median(), color='blue', linestyle='--', linewidth=2, label=f'Median: {df[var].median():.1f}')
            axes[idx].set_title(var.replace('_', ' ').title(), fontweight='bold')
            axes[idx].set_xlabel('Value')
            axes[idx].set_ylabel('Frequency')
            axes[idx].legend()
            axes[idx].grid(alpha=0.3)
    
    # Hide unused subplots
    for idx in range(len(available_vars), len(axes)):
        axes[idx].axis('off')
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

def render_risk_distribution(df):
    """Render pie chart of risk distribution"""
    risk_counts = df['risk'].value_counts()
    
    colors = {'🟢 Low Risk': '#0F9D58', '🟡 Moderate Risk': '#F4B400', '🔴 Elevated Risk': '#DB4437'}
    plot_colors = [colors.get(risk, '#999999') for risk in risk_counts.index]
    
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%',
                                        colors=plot_colors, startangle=90, textprops={'fontsize': 10})
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title("Risk Level Distribution", fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
