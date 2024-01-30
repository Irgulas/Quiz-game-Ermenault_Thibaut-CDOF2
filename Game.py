import json
def save_score(name, score):
    try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []

    scores.append({'name': name, 'score': score})
    
    with open('scores.json', 'w') as file:
        json.dump(scores, file)
#New Feature !!!
def run_quiz():
    # Questions categorisées par niveau de difficulté avec choix de réponses
    questions = {
        "facile": [
            {"question": "Quelle est la capitale de la France ?", "choices": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"], "answer": "A"},
            {"question": "Quelle est la formule chimique de l'eau ?", "choices": ["A. CO2", "B. H2O", "C. O2", "D. H2SO4"], "answer": "B"}
        ],
        "moyen": [
            {"question": "Qui a écrit 'Hamlet' ?", "choices": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"], "answer": "B"},
            {"question": "Quel est le plus grand océan du monde ?", "choices": ["A. Atlantique", "B. Indien", "C. Pacifique", "D. Arctique"], "answer": "C"}
        ],
        "difficile": [
            {"question": "Qui a peint la 'Joconde' ?", "choices": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Rembrandt"], "answer": "C"},
            {"question": "Qui a inventé l'ampoule électrique ?", "choices": ["A. Nikola Tesla", "B. Thomas Edison", "C. Alexander Graham Bell", "D. Albert Einstein"], "answer": "B"}
        ]
    }

    print("Choisissez un niveau de difficulté: facile, moyen, difficile")
    level = input().lower()

    if level not in questions:
        print("Niveau de difficulté non valide. Veuillez choisir entre facile, moyen, difficile.")
        return

    selected_questions = questions[level]
    score = 0

    for q in selected_questions:
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

    print(f"Votre score final est : {score}/{len(selected_questions)}")
    #print(f"Votre score final est : {score}/{len(questions)}")
    name = input("Entrez votre nom pour enregistrer votre score: ")
    save_score(name, score)
    display_leaderboard()

## Game
run_quiz()
