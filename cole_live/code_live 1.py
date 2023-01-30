# #Code live 1
# hours, minutes, seconds = input().split()
# print(hours)
# print(minutes)
# print(seconds)

hours = int(input())
minutes = int(input())
seconds = int(input())

total_seconds = hours * 3600 + 60 * minutes + seconds

print(f"Seconds: {total_seconds}")

# Convert from seconds
total_seconds = int(input())

hours = total_seconds // 3600
remain_seconds = total_seconds % 3600

minutes = remain_seconds // 60
remain_seconds %= 60

print("hours", hours)
print("minutes", minutes)
print("seconds" + str(remain_seconds))