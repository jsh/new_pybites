# Bite: Remove Emoji Prefix

In this Bite, you will write a function that takes a string and removes any emoji prefix from it, using the `str.removeprefix()` method introduced in Python 3.9. This is a great opportunity to explore some of the new string methods and build a function that can be used to sanitize user-generated text.

The function should work as follows:

```
>>> remove_emoji_prefix("🚀 Launch successful!")
'Launch successful!'

>>> remove_emoji_prefix("🐍 Python is awesome!")
'Python is awesome!'

>>> remove_emoji_prefix("🍕 Let's grab some lunch!")
"Let's grab some lunch!"
```

If the string does not begin with an emoji, the function should return the original string:

```
>>> remove_emoji_prefix("The quick brown fox jumps over the lazy dog.")
'The quick brown fox jumps over the lazy dog.'

>>> remove_emoji_prefix("🤖🚀 Python is the language of choice for AI development.")
'🤖🚀 Python is the language of choice for AI development.'
```

## Signature

```
def remove_emoji_prefix(text: str) -> str:
    pass
```

## Constraints

- The function should remove any emoji prefix present in the text.

- An emoji prefix is defined as a string that starts with an emoji character, followed by a space character.

- The text is guaranteed to be a non-empty string.
