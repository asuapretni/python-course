tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]
print(tags[:2])  # ['python', 'development']
slice_obj = slice(2)
print(slice_obj)  # slice(None, 2, None)
print(tags[slice_obj])  # ['python', 'development']

print(tags[1:4:2])  # same as below
slice_obj = slice(1, 4, 2)  # same as above
print(tags[slice_obj])

print(slice_obj.start)  # 1
print(slice_obj.stop)  # 4
print(slice_obj.step)  # 2