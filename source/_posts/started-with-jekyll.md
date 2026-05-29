---
title: "Getting Started with Jekyll"
date: 2026-05-29 09:38:27
categories:
  - tutorial
  - jekyll
tags:
  - jekyll
  - tutorial
  - static-site
  - github-pages
cover: /images/placeholder-cover.png
---

Welcome to the wonderful world of Jekyll! In this tutorial, we'll walk through the basics of creating a static website with Jekyll.

## What is Jekyll?

Jekyll is a static site generator that takes plain text files and converts them into a beautiful static website. It's perfect for blogs, documentation sites, and personal portfolios.

## Why Use Jekyll?

- **Simple**: No database required
- **Fast**: Static sites load quickly
- **Secure**: No server-side vulnerabilities
- **GitHub Pages**: Perfect for hosting on GitHub

## Getting Started

### Step 1: Install Jekyll

```bash
gem install jekyll bundler
```

### Step 2: Create a New Site

```bash
jekyll new my-awesome-site
cd my-awesome-site
```

### Step 3: Serve the Site

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` to see your site!

## Project Structure

A typical Jekyll project looks like this:

```
my-awesome-site/
├── _config.yml    # Configuration
├── _posts/        # Blog posts
├── _layouts/      # Page templates
├── _includes/     # Reusable components
├── index.md       # Home page
└── about.md       # About page
```

## Creating Your First Post

Create a new file in `_posts/` with the format `YYYY-MM-DD-title.md`:

```yaml
---
layout: post
title: "My First Post"
date: 2026-01-01 12:00:00
categories: [general]
---

Welcome to my first blog post!
```

## Conclusion

Jekyll is a powerful tool for creating static websites. With its simplicity and flexibility, it's no wonder it's the most popular static site generator.

Happy coding! 🚀
