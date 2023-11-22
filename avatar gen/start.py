from PIL import Image, ImageDraw
import random
import os

def generate_random_avatar(size=200):
    # Create a blank image with a white background
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)

    # Draw a random color rectangle
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.rectangle([0, 0, size, size], fill=color)

    # Draw a random pattern (e.g., circles)
    for _ in range(random.randint(5, 15)):
        x = random.randint(0, size)
        y = random.randint(0, size)
        radius = random.randint(5, 20)
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill="white")

    return image

def save_avatar(image, filename="pic file.png"):
    image.save(filename)
    print(f"Avatar saved to {filename}")

def main():
    # Generate and save multiple avatars without preview
    num_avatars = int(input("Enter the number of avatars to generate: "))
    base_filename = "pic file"

    for i in range(1, num_avatars + 1):
        # Generate a random avatar
        avatar = generate_random_avatar()

        # Save the avatar to a file with a unique filename
        filename = f"{base_filename}{i}.png"
        save_avatar(avatar, filename)

if __name__ == "__main__":
    main()
