import re

from app.models import SocialMediaPost as SocialMediaPostModel

def clean_text(text: str) -> str:
    """
    Clean social media text while preserving useful content.
    """

    # Remove leading/trailing whitespace
    text = text.strip()

    # Replace multiple whitespace characters with one space
    text = re.sub(r"\s+", " ", text)

    # Remove repeated exclamation/question marks
    text = re.sub(r"!{2,}", "!", text)
    text = re.sub(r"\?{2,}", "?", text)

    return text


def extract_hashtags(text: str) -> list[str]:
    """
    Extract hashtags from social media text.
    """

    hashtags = re.findall(r"#([A-Za-z0-9_]+)", text)

    return [tag.lower() for tag in hashtags]



def extract_hashtags(text: str) -> list[str]:
    """
    Extract hashtags from social media text.
    """

    hashtags = re.findall(r"#([A-Za-z0-9_]+)", text)

    return [tag.lower() for tag in hashtags]


def extract_mentions(text: str) -> list[str]:
    """
    Extract user mentions from social media text.
    """

    mentions = re.findall(r"@([A-Za-z0-9_]+)", text)

    return [mention.lower() for mention in mentions]


def normalize_platform(platform: str) -> str:
    """
    Normalize platform names.
    """

    return platform.strip().lower()

def preprocess_post(post: SocialMediaPostModel) -> dict:
    """
    Convert a raw database post into a processed representation.
    """

    clean_caption = clean_text(post.caption)

    hashtags = extract_hashtags(post.caption)

    mentions = extract_mentions(post.caption)

    platform = normalize_platform(post.platform)

    return {
        "post_id": post.post_id,
        "platform": platform,
        "user_id": post.user_id,
        "text": clean_caption,
        "hashtags": hashtags,
        "mentions": mentions,
        "likes": post.likes,
        "comments": post.comments,
        "shares": post.shares,
        "reach": post.reach,
        "timestamp": post.timestamp,
    }