import re

# 定義 pattern 和對應的處理函式
patterns = [
    #Data transfer instructions
    {
        #MOV @Ri, #imm
        'pattern': r'^\s*MOV\s*+@R(\d)\s*,\s*+#0*([0-9A-Fa-f]+)H\s*$',
        'action': lambda m: f"{format(0x76 + int(m.group(1)), '02X')} {format(int(m.group(2), 16), '02X')} "
    },
    {
        #MOV @Ri, direct
        'pattern': r'^\s*MOV\s*+@R(\d)\s*,\s*+0*([0-9A-Fa-f]+)H\s*$',
        'action': lambda m: f"{format(0xA6 + int(m.group(1)), '02X')} {format(int(m.group(2), 16), '02X')} "
    },
    {
        #MOV direct, Rn
        'pattern': r'^\s*MOV\s*+0*([0-9A-Fa-f]+)H\s*,\s*+R(\d)\s*$',
        'action': lambda m: f"{format(0x88 + int(m.group(2)), '02X')} {format(int(m.group(1), 16), '02X')} "
    },
    {
        #MOV Rn, #immediate
        'pattern': r'^\s*MOV\s*+R(\d)\s*,\s*+#0*([0-9A-Fa-f]+)H\s*$',
        'action': lambda m: f"{format(0x78 + int(m.group(1)), '02X')} {format(int(m.group(2), 16), '02X')} "
    },
    #Arithmetic & logic instructions
    {
        #ADD A, #imm
        'pattern': r'^\s*ADD\s*+A\s*,\s*+#0*([0-9A-Fa-f]+)H\s*$',
        'action': lambda m: f"24 {format(int(m.group(1), 16), '02X')} "
    },
    {
        #SUBB A, direct
        'pattern': r'^\s*SUBB\s*+A\s*,\s*+0*([0-9A-Fa-f]+)H\s*$',
        'action': lambda m: f"95 {format(int(m.group(1), 16), '02X')} "
    },
    {
        #ANL direct, #imm
        'pattern': r'^\s*ANL\s*+0*([0-9A-Fa-f]+)H\s*,\s*+#0*([0-9A-Fa-f]+)H\s*$',
        'action': lambda m: f"53 {format(int(m.group(1), 16), '02X')} {format(int(m.group(2), 16), '02X')} "
    },
    {
        #XRL direct, A
        'pattern': r'^\s*XRL\s*+0*([0-9A-Fa-f]+)H\s*,\s*+A\s*$',
        'action': lambda m: f"62 {format(int(m.group(1), 16), '02X')} "
    },
    #Branching instructions
    {
        #CJNE A, #imm, offset
        'pattern': r'^\s*CJNE\s*+A\s*,\s*+#0*([0-9A-Fa-f]+)H\s*,\s*+0*([0-9A-Fa-f]+)H\s*$',
        'action': lambda m: f"B4 {format(int(m.group(1), 16), '02X')} {format(int(m.group(2), 16), '02X')} "
    },
    {
        #DJNZ direct, offset
        'pattern': r'^\s*DJNZ\s*+0*([0-9A-Fa-f]+)H\s*,\s*+0*([0-9A-Fa-f]+)H\s*$',
        'action': lambda m: f"D5 {format(int(m.group(1), 16), '02X')} {format(int(m.group(2), 16), '02X')} "
    },
    #Null line
    {
        'pattern': r'^\s*$',
        'action': lambda m: f""
    },
]

output_lines = []

# 讀取 test01.txt
with open('test03.txt', 'r') as f:
    lines = f.readlines()

#逐行分析
for line in lines:
    line = line.strip()
    matched = False
    for p in patterns:
        match = re.match(p['pattern'], line)
        if match:
            result = p['action'](match)
            output_lines.append(result)
            matched = True
            break
    if not matched:
        output_lines.append(f"\n未識別指令：{line}\n")

# 輸出到 test01-out.txt
with open('test03-out.txt', 'w') as f:
    for out_line in output_lines:
        f.write(out_line)
