import random

PROMPT_TEMPLATES = {
    "image": {
        "prefixes": [
            "Generate an ultra-high-resolution, photorealistic masterpiece of",
            "Create a breathtaking, cinematic 8K scene depicting",
            "Produce a hyper-detailed, professional digital painting of",
            "Illustrate a dynamic character concept art for a AAA video game, showing",
            "Design an epic, sprawling landscape in the style of a fantasy epic, featuring",
            "Craft a stunning, award-winning photograph capturing the essence of",
            "Render a photorealistic architectural visualization of",
            "Create a vibrant and detailed splash art for a mobile game, featuring",
            "Generate a dark, atmospheric horror scene with intense detail, showing",
            "Produce a beautiful, intricate vector illustration suitable for a poster, depicting",
        ],
        "suffixes": [
            "rendered in Unreal Engine 5 with ray tracing and global illumination.",
            "with dramatic, volumetric lighting, creating long, soft shadows and a moody atmosphere.",
            "trending on ArtStation, showcasing incredible detail, sharp focus, and a cinematic feel.",
            "in the distinct, painterly style of Greg Rutkowski and James Gurney.",
            "shot on a 70mm lens, f/8, with a shallow depth of field and beautiful bokeh.",
            "featuring complex textures and materials, with a focus on realism and imperfections.",
            "composed with leading lines and a strong focal point to guide the viewer's eye.",
            "using a rich, cinematic color grade with deep contrasts and vibrant highlights.",
            "with a sense of epic scale and grandeur, making the subject feel immense.",
            "as a hyper-detailed macro shot, revealing intricate details not visible to the naked eye.",
        ],
    },
    "video": {
        "prefixes": [
            "Direct a cinematic, emotionally charged short film sequence about",
            "Produce a fast-paced, high-energy promotional video for a new tech product, showcasing",
            "Create a visually stunning 4K nature documentary clip in the style of Planet Earth, featuring",
            "Generate a professional, corporate training video that clearly explains",
            "Craft a suspenseful, horror-themed found-footage style video of",
            "Animate a clean, modern motion graphics explainer video about",
            "Shoot a beautiful, slow-motion video highlighting the details of",
            "Produce a dynamic, user-generated content style montage for social media, showing",
            "Direct a Wes Anderson-style symmetrical and quirky scene of",
            "Create a gritty, realistic action sequence with practical effects, involving",
        ],
        "suffixes": [
            "shot with anamorphic lenses for a classic widescreen cinematic look and feel.",
            "edited with dynamic J-cuts and L-cuts to create a seamless and engaging narrative flow.",
            "with professional sound design, including foley and an epic orchestral score.",
            "color graded to have a warm, inviting, and slightly desaturated look.",
            "featuring smooth, stabilized gimbal shots and breathtaking aerial drone footage.",
            "using kinetic typography and fluid transitions to keep the viewer engaged.",
            "filmed during the golden hour to achieve soft, natural, and flattering light.",
        ],
    },

    "code": {
        "prefixes": [
            "Develop a production-ready, highly scalable Python backend service that",
            "Write a clean, reusable, and well-documented React component library for",
            "Generate a highly optimized, memory-efficient C++ algorithm to",
            "Architect a complete, secure REST API using Node.js, Express, and PostgreSQL for",
            "Create a data processing pipeline in Python with Pandas and Dask for",
            "Write a suite of comprehensive end-to-end tests using Cypress for",
            "Develop a responsive, accessible, and pixel-perfect HTML/CSS frontend from a Figma design for",
            "Generate an optimized and indexed SQL schema and queries for",
            "Build a real-time multiplayer game server using WebSockets and Node.js for",
            "Create a custom, configurable webpack build for a complex frontend application that",
        ],
        "suffixes": [
            "following SOLID principles and including a full suite of unit and integration tests.",
            "that is fully compliant with WCAG 2.1 AA accessibility standards and optimized for Core Web Vitals.",
            "and include detailed, explanatory comments for all complex logic and data structures.",
            "with robust authentication, authorization, input validation, and detailed logging.",
            "ensuring the code is idempotent, fault-tolerant, and can handle massive datasets.",
            "and is deployed via a full CI/CD pipeline with automated checks and staging environments.",
            "with a focus on clean, semantic HTML and a modular BEM CSS architecture.",
            "designed to handle millions of records efficiently with minimal query latency.",
            "and implement a state synchronization mechanism to ensure a consistent game state for all clients.",
            "supports code splitting, tree shaking, and hot module replacement for an excellent developer experience.",
        ],
    },
    "other": {
        "prefixes": [
            "Compose a comprehensive, well-researched academic paper on the topic of",
            "Write a persuasive, emotionally resonant marketing campaign proposal for",
            "Generate a deeply engaging, character-driven short story set in a unique world where",
            "Draft a clear, concise, and easy-to-follow technical documentation for",
            "Create a script for a captivating 20-minute TED Talk about the future of",
            "Write a detailed, step-by-step business plan for a startup in the",
            "Compose a formal, legally sound cease and desist letter regarding",
            "Generate a thought-provoking, philosophical essay that explores the concept of",
            "Write the complete lyrics and chord progression for a folk-pop song about",
            "Draft a compelling and polished grant proposal to secure funding for",
        ],
        "suffixes": [
            "adopting a formal, scholarly tone and using APA 7th edition for all citations.",
            "written in a compelling, narrative style that connects with the target audience on an emotional level.",
            "structured with a strong narrative arc, including rising action, a climax, and a satisfying resolution.",
            "and include diagrams, code examples, and FAQs to make complex topics easily understandable.",
            "that uses powerful storytelling techniques to inspire and motivate the audience.",
            "including market analysis, financial projections, and a detailed operational plan.",
            "using precise, unambiguous language to clearly state the legal position and required actions.",
            "and present a balanced argument that considers multiple viewpoints and counterarguments.",
            "with a memorable chorus, a bridge that builds tension, and verses that tell a story.",
            "clearly outlining the project's objectives, methodology, budget, and expected impact.",
        ],
    }
}

def generate_prompt(goal: str, category: str = "other") -> str:
   
    category_templates = PROMPT_TEMPLATES.get(category.lower(), PROMPT_TEMPLATES["other"])

    prefix = random.choice(category_templates["prefixes"])
    suffix = random.choice(category_templates["suffixes"])

    final_prompt = f"{prefix} {goal} {suffix}"

    return final_prompt
