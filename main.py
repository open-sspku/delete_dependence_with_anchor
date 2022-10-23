# 删除锚定节点的依赖关系
# ---------------------------------------
# dot.txt文件是待过滤的文件
# 格式大致为
#
# digraph G{
# A -> C
# A -> B
# }
#
# 或者为
#
# A -> B
# A -> C
# ---------------------------------------
# anchor.txt文件是锚点文件
# 格式为
#
# Anchor1
# Anchor2
#
# 软件包名可以加引号
# ---------------------------------------
# new_dot.txt文件是输出文件
# ---------------------------------------
# 更改model的值，来删除依赖
# ---------------------------------------
with open('dot.txt') as f1:
    dot = f1.read().split('\n')
with open('anchor.txt') as f2:
    anchor = f2.read().split()
for i in range(len(anchor)):
    anchor[i] = anchor[i].strip(',')
    anchor[i] = anchor[i].strip('"')
with open('new_dot.txt','w') as f3:

    # 删除 锚点->其他             model 1
    # 删除 其他->锚点             model 2
    # 删除 锚点->其他 和 其他->锚点 model 3
    model = 1

    if model == 1:
        for dependence in dot:
            if '->' in dependence:
                data = dependence.split()
                package1 = data[0]
                package2 = data[-1].strip(';')
                if package1.strip('"') in anchor:
                    continue
            f3.write(dependence+'\n')

    if model == 2:
        for dependence in dot:
            if '->' in dependence:
                data = dependence.split()
                package1 = data[0]
                package2 = data[-1]
                if package2.strip('"') in anchor:
                    continue
            f3.write(dependence+'\n')

    if model == 3:
        for dependence in dot:
            if '->' in dependence:
                data = dependence.split()
                package1 = data[0]
                package2 = data[-1].strip(';')
                if package1.strip('"') in anchor or package2.strip('"') in anchor:
                    continue
            f3.write(dependence+'\n')
