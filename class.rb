class Post
  def initialize
    @content = "asdf"
  end

  def my_instance_method
    @content
  end

  def self.my_class_method
    puts "class method"
  end
end

p = Post.new
puts p.my_instance_method
Post.my_class_method