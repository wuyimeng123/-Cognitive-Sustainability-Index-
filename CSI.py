import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def cognitive_growth(t, k_g, tau_g, G_max=1.0):
    return G_max / (1 + np.exp(-k_g * (t - tau_g)))

def cognitive_atrophy(t, k_a, tau_a, A_max=1.0):
    return A_max / (1 + np.exp(-k_a * (t - tau_a)))

def cognitive_sustainability_index(t, mu, lambda_param, k_g, tau_g, k_a, tau_a):
    G_t = cognitive_growth(t, k_g, tau_g)
    A_t = cognitive_atrophy(t, k_a, tau_a)
    denominator = mu * G_t + lambda_param * A_t
    denominator[denominator == 0] = 1e-10
    return (mu * G_t) / denominator

def plot_cognitive_dynamics(ax, k_g, tau_g, k_a, tau_a, mu, lambda_param):
    t = np.linspace(0, 20, 500)
    G_t = cognitive_growth(t, k_g, tau_g)
    A_t = cognitive_atrophy(t, k_a, tau_a)
    CSI_t = cognitive_sustainability_index(t, mu, lambda_param, k_g, tau_g, k_a, tau_a)

    ax.clear()
    ax.plot(t, G_t, '#2B5B84', linewidth=2.5, label='认知增长')
    ax.plot(t, A_t, '#5A8CBF', linewidth=2.5, label='认知萎缩')
    ax.plot(t, CSI_t, '#8BC34A', linewidth=2.5, label='认知可持续性指数(CSI)')

    # 平衡区
    ax.axhline(y=0.55, color='#D3DEE8', linestyle=':', linewidth=2)
    ax.axhline(y=0.70, color='#D3DEE8', linestyle=':', linewidth=2)
    ax.fill_between(t, 0.55, 0.70, color='#D3DEE8', alpha=0.2, label='认知平衡区')

    ax.set_xlabel('时间 (t)', fontsize=12)
    ax.set_ylim(0, 1.05)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    
PRESETS = {
    "Studen": {
        "k_g": 0.5, "tau_g": 3.0,
        "k_a": 0.7, "tau_a": 5.0,
        "mu": 0.45, "lambda": 0.75
    },
    "Researcher": {
        "k_g": 0.8, "tau_g": 4.0,
        "k_a": 0.3, "tau_a": 6.0,
        "mu": 0.85, "lambda": 0.25
    },
    "AI-Assisted Expert": {
        "k_g": 0.8, "tau_g": 2.0,
        "k_a": 0.2, "tau_a": 6.0,
        "mu": 0.95, "lambda": 0.5
    }
}

st.set_page_config(page_title="Cognitive Sustainability Index", layout="wide")
st.title("Cognitive Sustainability Index ")

# 左侧控制区
with st.sidebar:
    st.header("参数控制")

    # 角色预设下拉菜单
    preset_name = st.selectbox("快速切换角色", list(PRESETS.keys()))
    preset = PRESETS[preset_name]

    st.markdown("---")
    st.subheader("手动调节参数")

    # 用滑块控件，并赋予预设默认值
    k_g = st.slider("认知增长速率 k_g", 0.1, 2.0, value=preset["k_g"], step=0.1)
    tau_g = st.slider("增长拐点 τ_g", 1.0, 10.0, value=preset["tau_g"], step=0.5)
    k_a = st.slider("认知萎缩速率 k_a", 0.1, 2.0, value=preset["k_a"], step=0.1)
    tau_a = st.slider("萎缩拐点 τ_a", 1.0, 15.0, value=preset["tau_a"], step=0.5)
    mu = st.slider("元认知调节 μ", 0.1, 1.0, value=preset["mu"], step=0.05)
    lambda_param = st.slider("自动化依赖 λ", 0.1, 1.0, value=preset["lambda"], step=0.05)

    # 显示当前参数组合（方便记录）
    st.markdown("---")
    st.caption(f"当前参数：k_g={k_g}, τ_g={tau_g}, k_a={k_a}, τ_a={tau_a}, μ={mu}, λ={lambda_param}")

# 右侧绘图区
fig, ax = plt.subplots(figsize=(10, 6))
plot_cognitive_dynamics(ax, k_g, tau_g, k_a, tau_a, mu, lambda_param)
st.pyplot(fig)

# 底部解释
st.markdown("""
---
**说明**：
- **CSI** ……
""")