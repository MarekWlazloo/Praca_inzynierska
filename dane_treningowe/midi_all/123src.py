# import os
# import pretty_midi

# def calculate_midi_duration(midi_file_path):
#     try:
#         midi_data = pretty_midi.PrettyMIDI(midi_file_path)
#         total_seconds = midi_data.get_end_time()
#         return total_seconds
#     except (ValueError, IndexError, EOFError, IOError, ZeroDivisionError, pretty_midi.MidiException) as e:
#         print(f"Ignorowanie problematycznego pliku {midi_file_path}: {str(e)}")
#         return 0

# def format_time(seconds):
#     minutes, seconds = divmod(seconds, 60)
#     return f"{int(minutes)} minut {int(seconds)} sekund"

# def main():
#     current_directory = os.getcwd()
#     midi_files = [file for file in os.listdir(current_directory) if file.endswith('.midi') or file.endswith('.mid')]
    
#     if not midi_files:
#         print("Brak plików MIDI w bieżącym katalogu.")
#         return

#     total_duration = 0

#     for midi_file_name in midi_files:
#         midi_file_path = os.path.join(current_directory, midi_file_name)
#         try:
#             duration = calculate_midi_duration(midi_file_path)
#             total_duration += duration
#         except Exception as e:
#             print(f"Błąd podczas przetwarzania pliku {midi_file_name}: {str(e)}")

#     formatted_total_duration = format_time(total_duration)

#     print(f"Liczba plików MIDI: {len(midi_files)}")
#     print(f"Łączna długość trwania: {formatted_total_duration}")


# main()


import os
import pretty_midi

def calculate_midi_duration(midi_file_path):
    try:
        midi_data = pretty_midi.PrettyMIDI(midi_file_path)
        total_seconds = midi_data.get_end_time()
        return total_seconds
    except Exception as e:
        print(f"Błąd podczas przetwarzania pliku {midi_file_path}: {str(e)}")
        return 0

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes)} minut {int(seconds)} sekund"

def main():
    current_directory = os.getcwd()
    midi_files = [file for file in os.listdir(current_directory) if file.endswith('.midi') or file.endswith('.mid')]
    
    if not midi_files:
        print("Brak plików MIDI w bieżącym katalogu.")
        return

    total_duration = 0

    for midi_file_name in midi_files:
        midi_file_path = os.path.join(current_directory, midi_file_name)
        duration = calculate_midi_duration(midi_file_path)
        total_duration += duration

    formatted_total_duration = format_time(total_duration)

    print(f"Liczba plików MIDI: {len(midi_files)}")
    print(f"Łączna długość trwania: {formatted_total_duration}")

main()










# import os
# import mido

# def calculate_midi_duration(midi_file_path):
#     try:
#         midi_file = mido.MidiFile(midi_file_path)
#         duration = 0
#         for track in midi_file.tracks:
#             for msg in track:
#                 if msg.type == 'note_on':
#                     duration += msg.time
#         return duration
#     except Exception as e:
#         print(f"Błąd podczas przetwarzania pliku {midi_file_path}: {str(e)}")
#         return 0

# def main():
#     current_directory = os.getcwd()
#     midi_files = [file for file in os.listdir(current_directory) if file.endswith('.midi') or file.endswith('.mid')]
    
#     if not midi_files:
#         print("Brak plików MIDI w bieżącym katalogu.")
#         return

#     total_duration = 0

#     for midi_file_name in midi_files:
#         midi_file_path = os.path.join(current_directory, midi_file_name)
#         duration = calculate_midi_duration(midi_file_path)
#         total_duration += duration

#     print(f"Liczba plików MIDI: {len(midi_files)}")
#     print(f"Łączna długość trwania: {total_duration / 1000:.2f} sekundy")


# main()
