import matplotlib.pyplot as plt
import numpy as np


def plot_soil_moisture(S_euler, S_rk4, S_optimal, params):
    """
    Plot soil moisture simulation results comparing Euler, RK4,
    and the optimized irrigation scenario.
    """
    days = list(range(len(S_euler)))

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(days, S_euler, label='Euler (no irrigation)', linewidth=1.8, linestyle='--', color='gray')
    ax.plot(days, S_rk4, label='RK4 (no irrigation)', linewidth=1.8, linestyle=':', color='steelblue')
    ax.plot(days, S_optimal, label='Optimized irrigation', linewidth=2, color='green')
    ax.axhline(params['min_moisture_pct'], color='red', linestyle='--',
               linewidth=1.2, label='min threshold (' + str(params['min_moisture_pct']) + '%)')
    ax.axhline(params['field_capacity_pct'], color='orange', linestyle='--',
               linewidth=1.2, label='field capacity (' + str(params['field_capacity_pct']) + '%)')
    ax.set_title('Soil Moisture — Zone A: Simulation and Optimized Schedule')
    ax.set_xlabel('Day')
    ax.set_ylabel('Soil Moisture (%)')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('../reports/final_soil_moisture.png', dpi=150)
    plt.show()


def plot_irrigation_schedule(irrigation, title='Optimized Daily Irrigation Schedule — Zone A'):
    """
    Bar chart of daily irrigation amounts.
    """
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.bar(range(len(irrigation)), irrigation, color='steelblue', alpha=0.8)
    ax.set_title(title)
    ax.set_xlabel('Day')
    ax.set_ylabel('Irrigation (mm)')
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('../reports/final_irrigation_schedule.png', dpi=150)
    plt.show()
