# Sales Dashboard Example
# Exemple de Tableau de Bord des Ventes
#
# A complete dashboard UI with header, metrics, and charts
# Un tableau de bord UI complet avec en-tête, métriques et graphiques
#
# Run: cypher run examples/dashboard.cypher
# Exécuter: cypher run examples/dashboard.cypher

# Main container / Conteneur principal
A(dashboard);T(flex;column):

  # Header section / Section en-tête
  A(header);G("Sales Dashboard");T(text-2xl;padding:1rem):

  # Metrics row / Ligne de métriques
  A(metrics);T(grid):
    
    # Revenue card / Carte revenu
    A(revenue_card);T(primary):
      G("Revenue");T(text-xl):
      G("$45,234");T(text-3xl;font-bold):
    
    # Users card / Carte utilisateurs
    A(users_card);T(primary):
      G("Active Users");T(text-xl):
      G("1,234");T(text-3xl;font-bold):
    
    # Orders card / Carte commandes
    A(orders_card);T(primary):
      G("Orders");T(text-xl):
      G("456");T(text-3xl;font-bold):

  # Chart section / Section graphique
  A(chart_section);T(flex):
    A(chart);G("Sales Chart Placeholder");T(text-center):

  # Footer / Pied de page
  A(footer);G("© 2026 CYPHER Corp");T(text-center;padding:1rem):

# Fix and launch / Fixer et lancer
F(fixed):
L(life):

# This generates a complete dashboard with:
# Ceci génère un tableau de bord complet avec:
# - Responsive grid layout / Mise en page grille responsive
# - Styled metric cards / Cartes de métriques stylisées  
# - Chart placeholder / Emplacement graphique
# - Professional appearance / Apparence professionnelle