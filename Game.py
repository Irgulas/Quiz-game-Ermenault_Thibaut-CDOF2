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
            {"question": "Quelle est la formule chimique de l'eau ?", "choices": ["A. CO2", "B. H2O", "C. O2", "D. H2SO4"], "answer": "B"},
            {"question": "Quel est le plus grand fleuve du monde ?", "choices": ["A. Nil", "B. Amazone", "C. Mississipi", "D. Yangtsé"], "answer": "B"},
            {"question": "Combien de continents y a-t-il sur Terre ?", "choices": ["A. 5", "B. 6", "C. 7", "D. 8"], "answer": "C"},
            {"question": "Quelle est la monnaie de l'Union européenne ?", "choices": ["A. Dollar", "B. Euro", "C. Yen", "D. Livre sterling"], "answer": "B"},
            {"question": "Quel est le plus grand lac d'Afrique ?", "choices": ["A. Lac Victoria", "B. Lac Tanganyika", "C. Lac Malawi", "D. Lac Albert"], "answer": "A"}
        ],
        "moyen": [
            {"question": "Qui a écrit 'Hamlet' ?", "choices": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"], "answer": "B"},
            {"question": "Quel est le plus grand océan du monde ?", "choices": ["A. Atlantique", "B. Indien", "C. Pacifique", "D. Arctique"], "answer": "C"},
            {"question": "Quelle est la monnaie officielle du Japon ?", "choices": ["A. Yen", "B. Won", "C. Dollar", "D. Euro"], "answer": "A"},
            {"question": "Combien de côtés a un octogone ?", "choices": ["A. 6", "B. 7", "C. 8", "D. 9"], "answer": "C"},
            {"question": "Qui a écrit 'Orgueil et Préjugés' ?", "choices": ["A. Charlotte Brontë", "B. Jane Austen", "C. Emily Brontë", "D. Charles Dickens"], "answer": "B"},
            {"question": "Quel est le plus long fleuve d'Amérique du Sud ?", "choices": ["A. Amazone", "B. Paraná", "C. Orénoque", "D. São Francisco"], "answer": "A"}
        ],
        "difficile": [
            {"question": "Qui a peint 'La Nuit étoilée' ?", "choices": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Claude Monet", "D. Édouard Manet"], "answer": "A"},
            {"question": "Qui a inventé la théorie de la relativité restreinte ?", "choices": ["A. Isaac Newton", "B. Albert Einstein", "C. Niels Bohr", "D. Max Planck"], "answer": "B"},
            {"question": "Quel est le plus grand animal terrestre ?", "choices": ["A. Éléphant", "B. Girafe", "C. Rhinocéros", "D. Hippopotame"], "answer": "A"},
            {"question": "Quelle est la capitale de l'Australie ?", "choices": ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Brisbane"], "answer": "B"},
            {"question": "Quel est le plus haut sommet d'Afrique ?", "choices": ["A. Kilimandjaro", "B. Mont Kenya", "C. Rwenzori", "D. Simien"], "answer": "A"},
            {"question": "Qui a découvert la pénicilline ?", "choices": ["A. Marie Curie", "B. Alexander Fleming", "C. Louis Pasteur", "D. Joseph Lister"], "answer": "B"}
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
