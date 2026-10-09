appointments = []


def book_appointment(patient, doctor, date, time):
    if not patient or not doctor or not date or not time:
        return "All fields are required"

    appointment = {
        "patient": patient,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    return "Appointment booked successfully"


def view_appointments():
    return appointments


def cancel_appointment(patient):
    for appointment in appointments:
        if appointment["patient"] == patient:
            appointments.remove(appointment)
            return "Appointment cancelled successfully"

    return "Appointment not found"


if __name__ == "__main__":
    print("ONLINE HOSPITAL APPOINTMENT BOOKING SYSTEM")
    print("------------------------------------------")

    patient = input("Enter patient name: ")
    doctor = input("Enter doctor name: ")
    date = input("Enter appointment date: ")
    time = input("Enter appointment time: ")

    result = book_appointment(patient, doctor, date, time)
    print(result)

    print("\nAppointment Details:")
    print(view_appointments())