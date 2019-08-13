class Post():
  def __init__(self):
    self.content = "asdf"

  def my_instance_method(self):
    return self.content

  @classmethod
  def my_class_method(cls):
    print("class method")

p = Post()
print(p.my_instance_method())
Post.my_class_method()