import matplotlib.pyplot as plt

'''
    Stack Plots: Graphical representation of datasets (trends)
    found throughout a set of data. These datasets are plotted
    on top of one another. All of this is with respect to time.
'''

days = [1, 2, 3, 4, 5, 6, 7]    # Monday to Sunday
sleeping = [7.5, 8.0, 8.0, 7.25, 9.0, 4.0, 10.0]    # All in hours
eating = [2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 2.0]
working = [7.5, 7.5, 7.5, 7.5, 7.5, 0, 0]
playing = [0, 0, 0, 0, 4.5, 10, 12]
other = [7, 6.5, 6.5, 4.25, 0, 7, 0]

plt.plot([],[],color="black", label ="Sleeping", linewidth=5)
plt.plot([],[],color="red", label ="Eating", linewidth=5)
plt.plot([],[],color="cyan", label ="Working", linewidth=5)
plt.plot([],[],color="purple", label ="Playing", linewidth=5)
plt.plot([],[],color="green", label ="Other", linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, other, colors=["black", "red", "cyan", "purple", "green"])

plt.xlabel("Day number in Week (From Monday to Sunday)")
plt.ylabel("Hours of a day")
plt.title("Number of Hours Given for an Activity in a Day")
plt.legend()
plt.show()