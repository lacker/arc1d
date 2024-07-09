import os

data_path = os.path.join(os.path.dirname(__file__), "data.txt")

def group_lines(is_separator, lines):
  groups = []
  pending_group = []
  for line in lines:
    if is_separator(line) and pending_group:
      groups.append(pending_group)
      pending_group = []
  if pending_group:
    groups.append(pending_group)
  return groups


def read():
  lines = []
  for line in open(data_path):
    if line.startswith("#"):
      continue
    lines.append(line)

  # TODO

      
