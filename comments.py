
coms = [
  {'name': 'alice', 'msg': ':)', 'replyto': None},
  {'name': 'bob', 'msg': ':0', 'replyto': None},
  {'name': 'claire', 'msg': ';)', 'replyto': None},
  {'name': 'alice', 'msg': '?', 'replyto': 2},
  {'name': 'claire', 'msg': '!!!', 'replyto': 2},
  {'name': 'bob', 'msg': 'OMG', 'replyto': 5},
  {'name': 'alice', 'msg': 'LOL', 'replyto': 6},
  {'name': 'claire', 'msg': ';)', 'replyto': 1},
  {'name': 'bob', 'msg': ';)', 'replyto': 1}
]

for idx in range(len(coms)):
  coms[idx]['id'] = idx + 1

class CommentTree:
  def __init__(self):
    self.id = None
    self.replies = []
    self.name = ""
    self.msg = ""

root = CommentTree()
root.name = "post"
def grow_comments(node, db, depth=0):
  replies = list(filter(lambda x: x['replyto'] == node.id, db))
  depth = depth + 1
  numrep = len(replies)
  reptext = 'reply' if numrep == 1 else 'replies'
  print(f'({numrep} {reptext} to {node.name})')
  for reply in replies:
    newTree = CommentTree()
    newTree.id = reply['id']
    user = list(filter(lambda x: x['id'] == newTree.id, replies))[0]
    newTree.name = user["name"]
    newTree.msg = user["msg"]
    node.replies.append(newTree)
    str = f'{"->"* depth} {newTree.name} tweeted {newTree.msg}'
    print(str)
    grow_comments(newTree, db, depth)

if __name__ == '__main__':   
  print(f'{len(coms)} COMMENTS')
  grow_comments(root, coms)