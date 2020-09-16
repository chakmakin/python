"""
Ouptput of the given line.
"""
out = file('output.txt','w')
out.write('Hello world\n')
out.write('how are you?')
out.close()
file('output.txt').read()