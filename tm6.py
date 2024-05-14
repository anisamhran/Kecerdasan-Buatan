# # import heapq

# # class State:
# #     def __init__(self, location, path_cost, heuristic):
# #         self.location = location
# #         self.path_cost = path_cost
# #         self.heuristic = heuristic

# #     def __lt__(self, other):
# #         return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)

# # class Graph:
# #     def __init__(self, graph_dict):
# #         self.graph_dict = graph_dict

# #     def heuristic(self, current, goal):
# #         # Implement your heuristic function here
# #         return 0

# #     def astar_search(self, start, goal):
# #         frontier = []
# #         heapq.heappush(frontier, State(start, 0, self.heuristic(start, goal)))
# #         explored = set()

# #         while frontier:
# #             current_state = heapq.heappop(frontier)
# #             current_location = current_state.location

# #             if current_location == goal:
# #                 return current_state.path_cost

# #             explored.add(current_location)

# #             for next_location, cost in self.graph_dict[current_location].items():
# #                 if next_location not in explored:
# #                     new_path_cost = current_state.path_cost + cost
# #                     new_state = State(next_location, new_path_cost, self.heuristic(next_location, goal))
# #                     heapq.heappush(frontier, new_state)

# #         return None

# # # Contoh penggunaan:
# # graph = Graph({
# #     'A': {'B': 1, 'C': 3},
# #     'B': {'A': 1, 'C': 1, 'D': 4},
# #     'C': {'A': 3, 'B': 1, 'D': 1},
# #     'D': {'B': 4, 'C': 1}
# # })

# # start_location = 'A'
# # goal_location = 'D'

# # shortest_path_cost = graph.astar_search(start_location, goal_location)
# # if shortest_path_cost is not None:
# #     print(f"Biaya perjalanan terpendek dari {start_location} ke {goal_location} adalah: {shortest_path_cost}")
# # else:
# #     print(f"Tidak ditemukan jalur yang memungkinkan dari {start_location} ke {goal_location}")

# class CareerPlanner:
#     def __init__(self, skills, education, goals):
#         self.skills = skills
#         self.education = education
#         self.goals = goals

#     def plan_career(self):
#         # Implement your career planning algorithm here
#         # Example career planning algorithm
#         recommended_career_path = []  # Construct the recommended career path
#         necessary_steps = []  # List of necessary steps to achieve career goals

#         # Example career planning logic based on user's skills, education, and goals
#         if "programming" in self.skills and "computer science degree" in self.education:
#             recommended_career_path.append("Software Engineer")
#             necessary_steps.append("Build portfolio projects")
#             necessary_steps.append("Apply for entry-level positions")
#             necessary_steps.append("Continue learning and gaining experience")

#         return recommended_career_path, necessary_steps

# # Example user preferences and information
# skills = ["programming", "problem-solving", "communication"]
# education = ["computer science degree"]
# goals = ["become a senior software engineer in 5 years"]

# # Initialize career planner
# planner = CareerPlanner(skills, education, goals)

# # Plan the career
# recommended_career_path, necessary_steps = planner.plan_career()

# # Output the planned career path
# if recommended_career_path:
#     print("Rencana Karir:")
#     print(f"Jalur Karir yang Direkomendasikan: {', '.join(recommended_career_path)}")
#     print("Langkah-langkah yang Diperlukan:")
#     for step in necessary_steps:
#         print(f"- {step}")
# else:
#  
# print("Maaf, tidak dapat merencanakan karir sesuai dengan informasi yang diberikan.")


# import pygame
# import sys

# # Inisialisasi Pygame
# pygame.init()

# # Lebar dan tinggi layar
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Missionaries and Cannibals")

# # Warna
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# BROWN = (165, 42, 42)

# # Fungsi untuk menggambar pulau, perahu, dan penumpang
# def draw_scene(left_bank, right_bank, boat_position):
#     screen.fill(WHITE)

#     # Draw pulau kiri
#     pygame.draw.rect(screen, GREEN, (100, 100, 200, 400))
#     pygame.draw.rect(screen, BROWN, (150, 300, 100, 200))
#     font = pygame.font.Font(None, 36)
#     text = font.render("Pulau 1", True, WHITE)
#     screen.blit(text, (150, 50))

#     # Draw pulau kanan
#     pygame.draw.rect(screen, GREEN, (500, 100, 200, 400))
#     pygame.draw.rect(screen, BROWN, (550, 300, 100, 200))
#     text = font.render("Pulau 2", True, WHITE)
#     screen.blit(text, (550, 50))

#     # Draw perahu
#     if boat_position == 0:
#         pygame.draw.rect(screen, BLUE, (400, 300, 100, 100))
#     else:
#         pygame.draw.rect(screen, BLUE, (300, 300, 100, 100))

#     # Draw penumpang di pulau kiri
#     for i in range(left_bank["missionaries"]):
#         pygame.draw.circle(screen, WHITE, (175, 400 - i * 50), 20)
#     for i in range(left_bank["cannibals"]):
#         pygame.draw.circle(screen, BLUE, (225, 400 - i * 50), 20)

#     # Draw penumpang di pulau kanan
#     for i in range(right_bank["missionaries"]):
#         pygame.draw.circle(screen, WHITE, (575, 400 - i * 50), 20)
#     for i in range(right_bank["cannibals"]):
#         pygame.draw.circle(screen, BLUE, (625, 400 - i * 50), 20)

#     pygame.display.flip()

# # Fungsi utama
# def main():
#     # Inisialisasi keadaan awal
#     left_bank = {"missionaries": 3, "cannibals": 3}
#     right_bank = {"missionaries": 0, "cannibals": 0}
#     boat_position = 0  # 0 untuk pulau kiri, 1 untuk pulau kanan

#     # Loop utama
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
#                 sys.exit()

#         # Gambar scene
#         draw_scene(left_bank, right_bank, boat_position)

#         # Dapatkan input pengguna
#         # Di sini Anda dapat menambahkan logika untuk mendapatkan input pengguna dan melakukan langkah-langkah yang sesuai

#         # Tampilkan perubahan
#         pygame.time.delay(1000)  # Delay sementara untuk memperlihatkan perubahan

# if __name__ == "__main__":
#     main()
