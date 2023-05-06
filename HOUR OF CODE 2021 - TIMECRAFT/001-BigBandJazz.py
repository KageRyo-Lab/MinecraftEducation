# Big Band Jazz (This is the Guided Challenge) 

# 提示：
# 爵士音樂家失去了他的小號，結果只剩卡祖笛可以演奏。
# 使用 agent.move() 函數穿過迷宮，然後使用 agent.collect() 取得小號。

# agent.move() 函數採用了一組參數：方向。
# 有效的方向為：
# 前進 (forward)
# 退後 (back)
# 向左 (left)
# 向右 (right)
# 向上 (up)
# 向下 (down)
# agent.collect() 函數未採用任何參數。

# 要求：
# 移動 Agent 穿越迷宮，找回小號。

# 比較簡單的做法
# 直接逐格移動
agent.move("forward")
agent.move("forward")
agent.move("forward")
agent.move("down")
agent.move("down")
agent.move("forward")
agent.move("forward")
agent.move("up")
agent.move("forward")
agent.move("forward")
agent.move("up")
agent.move("up")
agent.move("forward")
agent.move("forward")
agent.collect()

# 比較進階的做法
# 使用 for 迴圈來執行重複的動作
# 就像剛剛測試區一樣，重複的動作我們可以使用 for 迴圈來幫助我們更快的執行。
# 需要注意的是當只有執行一次的動作就不需要使用 for 迴圈包住了！
for i in range(3):
    # 前進三格
    agent.move("forward")
for i in range(2):
    # 往下兩格
    agent.move("down")
for i in range(2):
    # 前進兩格
    agent.move("forward")
    
# 往上一格
agent.move("up")

for i in range(2):
    # 前進兩格
    agent.move("forward")
for i in range(2):
    # 往上兩格
    agent.move("up")
for i in range(2):
    # 前進兩格
    agent.move("forward")
    
# 取得
agent.collect()