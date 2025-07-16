def extract_keywords(text, skill_keywords):
    found_skills = []
    text_lower = text.lower()
    
    for keyword in skill_keywords:
        if keyword.lower() in text_lower:
            found_skills.append(keyword)
    
    return list(set(found_skills))
