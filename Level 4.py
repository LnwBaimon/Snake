            if current_level == 4:
               current_time = time.time()

            if current_time - bomb_spawn_time >= bomb_spawn_interval:
                bomb_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (hight // 10)) * 10]
            
            if not hearts:
                heart_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (hight // 10)) * 10]
                hearts.append(heart_pos)
            
            if lucky_box is None:
                lucky_box_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (hight // 10)) * 10]
                lucky_box = lucky_box_pos

            if ai_direction == "UP":
                ai_snake_pos1[1] -= 10
            elif ai_direction == "DOWN":
                ai_snake_pos1[1] += 10
            elif ai_direction == "LEFT":
                ai_snake_pos1[0] -= 10
            elif ai_direction == "RIGHT":
                ai_snake_pos1[0] += 10

            if ai_direction1 == "UP":
                ai_snake_pos2[1] -= 10
            elif ai_direction1 == "DOWN":
                ai_snake_pos2[1] += 10
            elif ai_direction1 == "LEFT":
                ai_snake_pos2[0] -= 10
            elif ai_direction1 == "RIGHT":
                ai_snake_pos2[0] += 10

            # ตรวจสอบการชนขอบ
            if ai_snake_pos1[0] < 0 or ai_snake_pos1[0] >= width or ai_snake_pos1[1] < 0 or ai_snake_pos1[1] >= hight:
                ai_direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])  # สุ่มทิศทางใหม่เมื่อชนขอบ

            # เพิ่มส่วนของ AI Snake
            ai_snake_body1.insert(0, list(ai_snake_pos1))
            ai_snake_body1.pop()

            # เปลี่ยนทิศทาง AI Snake หลังจากเคลื่อนที่
            if random.random() < 0.05:  # โอกาสในการเปลี่ยนทิศทาง 5%
                ai_direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

            # ตรวจสอบการชนขอบ ตัวที่ 2
            if ai_snake_pos2[0] < 0 or ai_snake_pos2[0] >= width or ai_snake_pos2[1] < 0 or ai_snake_pos2[1] >= hight:
                ai_direction1 = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])  # สุ่มทิศทางใหม่เมื่อชนขอบ

            # เพิ่มส่วนของ AI Snake
            ai_snake_body2.insert(0, list(ai_snake_pos2))
            ai_snake_body2.pop()

            # เปลี่ยนทิศทาง AI Snake หลังจากเคลื่อนที่
            if random.random() < 0.05:  # โอกาสในการเปลี่ยนทิศทาง 5%
                ai_direction1 = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
                
            # Event เมื่อเก็บ Lucky block
            if lucky_box and snake_pos == lucky_box:
            lucky_box = None  
            lucky_item = random.choice(["score", "level_up", "speed_up", "restart"])

            if lucky_item == "score":
                bonus = random.randint(5, 7)
                score += bonus
            elif lucky_item == "level_up":
                if current_level < len(level_thresholds):
                    current_level += 1
            elif lucky_item == "speed_up":
                snake_speed += 20
            elif lucky_item == "restart":
                score = 0
                current_level = 1
                snake_speed = 10
                snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
            # Ai snake ตัวที่ 2
            ai_snake_pos2 = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (hight // 10)) * 10]
            ai_snake_body2 = [[ai_snake_pos1[0], ai_snake_pos1[1]], [ai_snake_pos1[0] - 10, ai_snake_pos1[1]], [ai_snake_pos1[0] - 20, ai_snake_pos1[1]], [ai_snake_pos1[0] - 30, ai_snake_pos1[1]]]
            ai_direction1 = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
