import os
import django
from django.contrib.auth.models import User
from blog.models import Post

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

def create_users():
    users_data = [
        {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'},
        {'username': 'user2', 'email': 'user2@example.com', 'password': 'password123'},
        {'username': 'user3', 'email': 'user3@example.com', 'password': 'password123'},
    ]

    for user_data in users_data:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )
            print(f"Created user: {user.username}")

def create_posts():
    posts_data = [
        {'title': 'The Future of AI', 'content': 'Artificial Intelligence is shaping the future of technology...', 'author': 'user1'},
        {'title': 'Benefits of Morning Exercise', 'content': 'Starting your day with a workout boosts energy...', 'author': 'user1'},
        {'title': 'Top 10 Python Libraries', 'content': 'Python offers a wide range of libraries like NumPy, Pandas...', 'author': 'user1'},
        {'title': 'How to Stay Productive', 'content': 'Effective time management techniques to boost productivity...', 'author': 'user1'},
        {'title': 'The Rise of Remote Work', 'content': 'Working from home is becoming the new normal...', 'author': 'user1'},
        {'title': 'Best Practices in Web Development', 'content': 'Writing clean and efficient code for scalable web apps...', 'author': 'user1'},
        {'title': 'Healthy Eating Habits', 'content': 'A balanced diet is essential for a healthy lifestyle...', 'author': 'user1'},
        {'title': 'Understanding Stock Market Trends', 'content': 'How to analyze trends and make informed investments...', 'author': 'user1'},
        {'title': 'How to Improve Communication Skills', 'content': 'Effective communication is key in personal and professional life...', 'author': 'user2'},
        {'title': 'The Power of Positive Thinking', 'content': 'A positive mindset can lead to greater success and happiness...', 'author': 'user2'},
        {'title': 'Best Travel Destinations in 2025', 'content': 'Explore the most exciting places to visit next year...', 'author': 'user2'},
        {'title': 'How to Build a Personal Brand', 'content': 'Your brand defines your presence in the digital world...', 'author': 'user2'},
        {'title': 'The Evolution of Smartphones', 'content': 'From early mobile phones to modern smartphones...', 'author': 'user2'},
        {'title': 'How to Overcome Procrastination', 'content': 'Practical tips to stay focused and productive...', 'author': 'user2'},
        {'title': 'The Science Behind Meditation', 'content': 'How meditation improves mental and physical health...', 'author': 'user2'},
        {'title': 'The Benefits of Reading Books', 'content': 'Reading enhances knowledge and improves cognitive skills...', 'author': 'user3'},
        {'title': 'How to Learn a New Language', 'content': 'Effective methods for mastering a foreign language...', 'author': 'user3'},
        {'title': 'The Role of Music in Our Lives', 'content': 'Music influences our emotions and daily experiences...', 'author': 'user3'},
        {'title': 'Time Management for Students', 'content': 'Balancing studies, work, and personal life effectively...', 'author': 'user3'},
        {'title': 'Introduction to Blockchain Technology', 'content': 'How blockchain is transforming industries worldwide...', 'author': 'user3'},
        {'title': 'The Psychology of Habits', 'content': 'Understanding how habits are formed and changed...', 'author': 'user3'},
        {'title': 'How to Achieve Financial Freedom', 'content': 'Strategies to manage money and build wealth...', 'author': 'user3'},
    ]

    for post_data in posts_data:
        author = User.objects.get(username=post_data['author'])
        if not Post.objects.filter(title=post_data['title']).exists():
            post = Post.objects.create(
                title=post_data['title'],
                content=post_data['content'],
                author=author
            )
            print(f"Created post: {post.title}")

if __name__ == '__main__':
    create_users()
    create_posts()