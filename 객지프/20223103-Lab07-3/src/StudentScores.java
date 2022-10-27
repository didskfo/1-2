public class StudentScores {
	private final int MAX_STUDENTS = 100;
	private String[] names;
	private int[] scores;
	private int numStudents;
	private Student students[];
	private String str_num;

	public StudentScores() {
		scores = new int[MAX_STUDENTS];
		names = new String[MAX_STUDENTS];
		numStudents = 0;
		students = new Student[MAX_STUDENTS];
	}

	public void add(String name, int score) {
		if (numStudents >= MAX_STUDENTS)
			return; // not enough space to add new student score
		students[numStudents] = new Student(name, score);
		numStudents++;
	}

	public String getHighest() {
		if (numStudents == 0)
			return null;

		int highest = 0;

		for (int i = 1; i < numStudents; i++)
			if (students[i].score() > students[highest].score())
				highest = i;
		str_num = Integer.toString(students[highest].score());

		return students[highest].name() + " " + str_num;
	}

	public String getLowest() {
		if (numStudents == 0)
			return null;

		int lowest = 0;

		for (int i = 1; i < numStudents; i++)
			if (students[i].score() < students[lowest].score())
				lowest = i;
		str_num = Integer.toString(students[lowest].score());

		return students[lowest].name() + " " + str_num;
	}
}
