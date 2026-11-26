# A246479：全部大字母表的列递推

**证明署名：** Chain.Ren · 独立研究 · [完整证明](PROOF.md) · 版本日期：2026-11-26

[固定版本证明](https://github.com/Asakitan/oeis-a246479/blob/proof-v1.0.0/PROOF.md) · [GitHub Release 与公开时间](https://github.com/Asakitan/oeis-a246479/releases/tag/proof-v1.0.0) · [引用信息](CITATION.cff)

证明 Robert Israel 的两条参数递推：奇数 $k\ge5$ 时四阶，偶数 $k\ge6$ 时十阶。这里 $k$ 是目标和值，也是字母表最大值；对每个这样的 $k$，递推在所有合法长度下成立。

[OEIS 原条目](https://oeis.org/A246479/internal) · [完整证明](PROOF.md) · [MIT 许可证](LICENSE)

## 复核

```sh
python -B verify.py
```

脚本仅需 Python 3.9+ 标准库。它用精确整数检查一个已知次数上界的矩阵多项式恒等式，而不是从有限个串长拟合递推。

本仓库给出可复核证明；不主张已经核定首证优先权。
