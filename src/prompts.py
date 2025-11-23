def build_caption_prompt(details: dict, tone: str = "luxury") -> str:
    base = f"""
You are an expert real estate copywriter.

Write a {tone} social media caption for this property:
- BHK: {details['bhk']}
- Area: {details['area']} sq ft
- Location: {details['location']}
- Highlights: {details['highlights']}
- View: {details.get('view', 'N/A')}

Keep it within 2–3 sentences, engaging, and suited for Instagram.
Return only the caption.
"""
    return base.strip()
