def run_quiz():
    questions = [
        {"question": "Quelle est la capitale de la France ?", "choices": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"], "answer": "A"},
        {"question": "Combien font 5 + 7 ?", "choices": ["A. 10", "B. 12", "C. 14", "D. 15"], "answer": "B"},
        {"question": "Quelle planète est connue comme la Planète Rouge ?", "choices": ["A. Terre", "B. Mars", "C. Jupiter", "D. Vénus"], "answer": "B"},
        {"question": "Qui a écrit 'Hamlet' ?", "choices": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"], "answer": "B"},
        {"question": "Quelle est la plus longue rivière du monde ?", "choices": ["A. Nil", "B. Amazone", "C. Mississippi", "D. Yangtsé"], "answer": "B"},
        {"question": "Qui a peint la 'Joconde' ?", "choices": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Rembrandt"], "answer": "C"},
        {"question": "Quelle est la formule chimique de l'eau ?", "choices": ["A. CO2", "B. H2O", "C. O2", "D. H2SO4"], "answer": "B"},
        {"question": "Quel est le plus grand océan du monde ?", "choices": ["A. Atlantique", "B. Indien", "C. Pacifique", "D. Arctique"], "answer": "C"},
        {"question": "Qui a inventé l'ampoule électrique ?", "choices": ["A. Nikola Tesla", "B. Thomas Edison", "C. Alexander Graham Bell", "D. Albert Einstein"], "answer": "B"},
        {"question": "Quel animal est connu comme le roi de la jungle ?", "choices": ["A. Éléphant", "B. Tigre", "C. Lion", "D. Gorille"], "answer": "C"}
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Entrez votre réponse (A, B, C, ou D) : ").strip().upper()
        if answer == q["answer"]:
            print("Correct !")
            score += 1
        else:
            print("Mauvaise réponse.")
        print()

    print(f"Votre score final est : {score}/{len(questions)}")
