# my solution
def better_than_average(class_points, your_points):
  average_score = sum(class_points) / len(class_points)
  return True if your_points > average_score else False

# better solution
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)
