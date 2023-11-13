title = input()
content = input()
comment = input()
print(f'<h1>\n'
      f'    {title}\n'
      f'</h1>')
print(f'<article>\n'
      f'    {content}\n'
      f'</article>')
while comment != 'end of comments':
    print(f'<div>\n'
          f'    {comment}\n'
          f'</div>')
    comment = input()
