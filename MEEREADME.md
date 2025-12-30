# Microcosmic Expansion Equation (MEE) 示例

def mee_next(U_n, F_x, infinity_branch=True, eta_min=0.001):
    """
    简化数值模拟版本（无穷分支用大数近似）
    """
    # 状态融合（这里用简单加法代替 ⊕）
    fusion = U_n + F_x
    
    # 无穷分支项（用一个极大值模拟）
    inf_branch = 1e12 if infinity_branch else 0
    
    # 最小扰动（噪声）
    import numpy as np
    noise = eta_min * np.random.randn()
    
    U_next = U_n + fusion + inf_branch + noise  # 简化并行为加法
    return U_next

# 示例运行
U_0 = 1.0
for step in range(5):
    U_0 = mee_next(U_0, F_x=2.5)
    print(f"Step {step+1}: U = {U_0}")
