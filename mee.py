import numpy as np

def mee_step(U_n, F_x, infinity_branch=True, eta_min=0.001):
    """
    Microcosmic Expansion Equation (MEE) 单步迭代
    
    U_{n+1} = U_n ∥ (U_n ⊕ F(x) + ∞-branch + η_min)
    
    这里用数值方式简化模拟：
    - ∥ 并行扩张 → 用加法近似（实际可替换为张量并行等）
    - ⊕ 状态融合 → 用加法 + 非线性激活模拟
    - ∞-branch → 用一个极大值模拟无穷分支
    - η_min → 最小噪声注入
    """
    # 状态融合 U_n ⊕ F(x)
    fusion = U_n + np.tanh(F_x)  # 示例非线性融合
    
    # 无穷分支项
    inf_branch = 1e12 if infinity_branch else 0
    
    # 最小扰动（生存不确定性）
    noise = eta_min * np.random.randn(*U_n.shape) if isinstance(U_n, np.ndarray) else eta_min * np.random.randn()
    
    # 并行扩张（这里简化用加法，实际可扩展为多分支并行）
    U_next = U_n + (fusion + inf_branch + noise)
    
    return U_next


# ==================== 示例运行 ====================
if __name__ == "__main__":
    # 初始状态（可以是标量或向量）
    U_0 = np.array([1.0])
    F_x = 2.5  # 示例生成函数输出
    
    print("MEE 迭代演示（5步）:")
    U_current = U_0.copy()
    for step in range(1, 6):
        U_current = mee_step(U_current, F_x, infinity_branch=True, eta_min=0.01)
        print(f"Step {step}: U = {U_current[0]:.4f}")
    
    # 输出说明：因为有 ∞-branch，数值会迅速趋向极大（模拟无限扩张）
