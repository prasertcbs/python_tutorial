# %% [markdown]
# # dictionary creation techniques

# %%
d={'th': 'Thailand', 'jp': 'Japan', 'kr': 'Korea'}
print(d)

# %%
en=['Thailand', 'Japan', 'Korea']
th=['ไทย', 'ญี่ปุ่น', 'เกาหลีใต้']
d2=dict(zip(en, th))
print(d2)

# %%
s=list('abcdef')
d3=dict.fromkeys(s, 0)
print(d3)

# %%
countries=[('th', 'Thailand'), ('jp', 'Japan'), ('kr', 'Korea')]
d4=dict(countries)
print(d4)

# %%


# %%
