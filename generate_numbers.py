import random

def generate_phone_numbers():
    # 定义一些主要国家的电话号码格式
    formats = [
        # 中国手机 (+86)
        lambda: f"86{random.choice(['13','14','15','16','17','18','19'])}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}",
        # 美国/加拿大 (+1)
        lambda: f"1{random.randint(2,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(2,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}",
        # 英国 (+44)
        lambda: f"44{random.randint(7,7):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}",
        # 日本 (+81)
        lambda: f"81{random.randint(7,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}",
        # 韩国 (+82)
        lambda: f"82{random.choice(['10'])}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}{random.randint(0,9):01d}",
    ]
    
    # 生成200个号码
    numbers = set()  # 使用集合确保号码唯一
    while len(numbers) < 200:
        format_func = random.choice(formats)
        numbers.add(format_func())
    
    return sorted(numbers)

def save_to_file(numbers, filename='phone_numbers.txt'):
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(f"{number}\n")

if __name__ == "__main__":
    numbers = generate_phone_numbers()
    save_to_file(numbers)
    print(f"已生成 {len(numbers)} 个电话号码并保存到 phone_numbers.txt") 