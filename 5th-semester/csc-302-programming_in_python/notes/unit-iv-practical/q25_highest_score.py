def get_topper(student_mark: dict[str, int]) -> dict[str, int]:
  topper_name: str = max(student_mark, key=student_mark.get)
  return {topper_name: student_mark[topper_name]}


if __name__ in '__main__':
  assert get_topper({'Alice': 85, 'Bob': 92, 'Charlie': 78}) == {'Bob': 92} 