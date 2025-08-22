import tkinter as tk
from asammdf import MDF
from rich import print as print_
from tkinter import ttk, filedialog
import time, math, random
import matplotlib.pyplot as plt


def gen(text: str, style: str):
    """This program is used to generate strings to print in sytl
    Eg - print_(gen("Error occured :( , failure not found!", 'bold #ff471a'))"""
    output = "[{}]{}[/{}]".format(style, text, style)
    return output


def show_banner(version="4.20"):
    """Displays a randomly selected banner with the provided version number."""
    banners = [
        """
 8888888b.        d8888  .d8888b.              d8888                   888                                    888 
 888  "Y88b      d88888 d88P  Y88b            d88888                   888                                    888 
 888    888     d88P888 Y88b.                d88P888                   888                                    888 
 888    888    d88P 888  "Y888b.            d88P 888 88888b.   8888b.  888 888  888 88888888  .d88b.  888d888 888 
 888    888   d88P  888     "Y88b.         d88P  888 888 "88b     "88b 888 888  888    d88P  d8P  Y8b 888P"   888 
 888    888  d88P   888       "888        d88P   888 888  888 .d888888 888 888  888   d88P   88888888 888     Y8P 
 888  .d88P d8888888888 Y88b  d88P       d8888888888 888  888 888  888 888 Y88b 888  d88P    Y8b.     888      "  
 8888888P" d88P     888  "Y8888P"       d88P     888 888  888 "Y888888 888  "Y88888 88888888  "Y8888  888     888 
                                                                                888                               
                                                                           Y8b d88P                               
                                                                            "Y88P"                                
 
        """,]
    separator = '[bold #00ff00]-+-[/bold #00ff00]' * 36
    selected_banner = random.choice(banners)
    print_(f"\n\n{separator}{gen(f"\n{selected_banner}", "bold #00ffff")}\nVersion - {version}\n{separator}")
#---------------------------------------------------------------------------------------------------------------------------------------
def quote_rmoval(t):
    """If a string contains quotes, this function removes it."""
    x = str()
    for i in t:
        if i in ["'",'"']:
            pass
        else:
            x += i
    return x
#---------------------------------------------------------------------------------------------------------------------------------------
def das_log_path_fetch():
    try:
        print_("\n{}{}\n".format(gen('---> ', 'bold #FEFA02'), gen("Press Enter key to manually select the DAS log.", 'bold #00ffff')))

        delay = input()
        print('\n')
        # Case 2
        path = filedialog.askopenfilename()
        if (path[-4:] == '.mf4'):
                print_(f"[bold #00ff00]{"Path fetch successful !"}[/bold #00ff00]")
                print("Kindly wait till the DAS log is being read...\n")
                return path
        else:
             print_(gen("Invalid path/ file !", 'bold #ff471a'))
             exit()

    except:
        print_(gen("Error occured while reading DAS MF4 log!\nPlease try again!", 'bold #ff471a'))
        exit()
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Helper functions - 
# ---------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

def generate_sample_dict(samples : list) -> dict:
    """
    Generate a dictionary where keys are unique values from the `samples` list, 
    and values are lists of indices where those values occur in `samples`.

    Parameters:
        samples (list): A list of elements (e.g., integers, strings) representing signal data.

    Returns:
        dict: A dictionary where each key is a unique value from `samples`,
              and the corresponding value is a list of indices in `samples`.

    Example:
        >>> samples = ["a", "b", "a", "c", "b", "a"]
        >>> generate_sample_dict(samples)
        {"a": [0, 2, 5], "b": [1, 4], "c": [3]}
    """
    # Initialize the dictionary
    sample_dict = {value: [] for value in set(samples)}

    # Populate indices for each value
    for idx, value in enumerate(samples):
        sample_dict[value].append(idx)

    return sample_dict
#---------------------------------------------------------------------------------------------------------------------------------------
def DAS_log_path_fetch():
    try:
        print_("\n{}{}\n".format(gen('---> ', 'bold #FEFA02'), gen("Press Enter key to manually select the DAS log.", 'bold #00ffff')))

        delay = input()
        print('\n')
        # Case 2
        path = filedialog.askopenfilename()
        if (path[-4:] == '.mf4'):
                path_short = path.split('/')[-1]
                print_(f"[bold #00ff00]{f"DAS Path {gen(path_short, 'bold #FE9900')} fetch successful !"}[/bold #00ff00]")
                print("Kindly wait till the DAS log is being read...\n")
                return path
        else:
             print_(gen("Invalid path/ file !", 'bold #ff471a'))
             exit()

    except:
        print_(gen("Error occured while reading DAS MF4 log!\nPlease try again!", 'bold #ff471a'))
        exit()
#---------------------------------------------------------------------------------------------------------------------------------------
def DMD_path_fetch():
    try:
        current_dir = os.getcwd() # fetches the path of the current working directory
        current_dir_contents = os.listdir(current_dir) # stores all the files & folders present in the current working directory
        print_("\n{}{}".format(gen('---> ', 'bold #FEFA02'), gen("Press Enter key if the DMD path is mentioned in the path.txt file", 'bold #00ffff')))
        print_("{}{}\n".format(gen('---> ', 'bold #FEFA02'), gen("Press '+' key & enter key to manually select the DMD.", 'bold #00ffff')))

        path = input('Enter your choice or path : ')
        print('\n')

        # Case 1 - when path.txt is present & the user enters just a blank space or hits enter
        if ('DMD_path.txt' in current_dir_contents) and (path in ["", ' ',]):
                with open("./DMD_path.txt", 'r') as fh:
                    path = quote_rmoval(fh.readline())
                    print_("Default path used: [purple]{}[/purple]".format(path))
                    print_(f"[bold #00ff00]{"\nDMD path fetch successful !"}[/bold #00ff00]")
                    print_(f"{gen("\nReading Data from DMD...", "#A7FF03")}")
                    return path
        # Case 2
        elif (path == "+"):
                path = filedialog.askopenfilename()
                path_short = path.split('/')[-1]
                print_(gen(f"\nDMD path : {gen(path_short, 'bold #FE9900')} fetch successful !", "bold #00ff00"))
                print_(f"{gen("\nReading Data from DMD...", "#A7FF03")}")
                return path
        else:
             print_(gen("Invalid path!", 'bold #ff471a'))
             exit()

    except:
        print_(gen("Error occured while reading DMD!\nPlease try again!", 'bold #ff471a'))
        exit()
#---------------------------------------------------------------------------------------------------------------------------------------
def find_set_cur_failures(cur_failure_list : list) -> list:
    """
    Identifies and returns a list of failure names where the failure is set (i.e., non-zero values in 'samples').

    Args:
        log_data_trimmed (list): A list of dictionaries where each dictionary represents a signal with keys 
                                 'name', 'samples', 'timestamps', 'unit','plot' and 'changes.

    Returns:
        list: A list of failure names (from 'name' field) where the failure condition is detected (non-zero in 'samples').
        note: channel['transition_data'] = (transition_indices, transition_flag, constant_value)
    """
    cur_failures_set = []
    
    # Loop through each channel in cur_failure_list
    for index, channel in enumerate(cur_failure_list):
        if channel['transition_data'][1] == True or str(channel['transition_data'][2]) == '1':
            cur_failures_set.append((index, channel))

    
    return cur_failures_set
#---------------------------------------------------------------------------------------------------------------------------------------
def find_set_fin_failures(fin_failure_list : list) -> list:
    """
    Identifies and returns a list of failure names where the failure is set (i.e., non-zero values in 'samples').

    Args:
        log_data_trimmed (list): A list of dictionaries where each dictionary represents a signal with keys 
                                 'name', 'samples', 'timestamps', 'unit','plot' and 'changes.

    Returns:
        list: A list of failure names (from 'name' field) where the failure condition is detected (non-zero in 'samples').
        note: channel['transition_data'] = (transition_indices, transition_flag, constant_value)
    """
    fin_failures_set = []
    
    # Loop through each channel in fin_failure_list
    for index, channel in enumerate(fin_failure_list):
        if channel['transition_data'][1] == True or str(channel['transition_data'][2]) == '1':
            fin_failures_set.append((index, channel))
    
    return fin_failures_set
#---------------------------------------------------------------------------------------------------------------------------------------
def capture_transitions(channel : dict) -> tuple:
    """
    Functions which takes in a channel & returns a list which contains the indices in which the tranistion occured.
     Args:
        channel (dict): a direct channel from the mdf file.
    Returns:
        tuple: (transition_indices, transition_flag, constant_value)
        transition_indices - a tuple whose elemetns are a list which contains the incices at which the transition occurs, 
        transition_flag - a boolean variable whose vaule is set to 1 when there is a change in it's sample values &
        constant_value - if the value is not changed at all, it returns the value which is present thoughout for that channel
    """
    transition_indices = []
    transition_flag : bool = False
    constant_value = None
    
    # Process the samples in one pass
    previous_sample = channel.samples[0]  # Start with the first sample

    for i, sample in enumerate(channel.samples):
        # # Check if the sample is a set failure (non-zero)
        # if sample != 0:
        #     channel_result['set_failures'].append(i)

        # Check for changes in the samples (compared to the previous sample)
        if i > 0 and sample != previous_sample:
            transition_indices.append(i)

        # Update previous sample for the next iteration
        previous_sample = sample
    
    if len(transition_indices) != 0:
        transition_flag = True
    
    if transition_flag == False:
        constant_value = channel.samples[0]
    
    return (transition_indices, transition_flag, constant_value)
#---------------------------------------------------------------------------------------------------------------------------------------

def DAS_log_initialization(path, DMD_control_functions, DMD_warning_lamps, additonal_channel_req):

    '''
    Note - 
    Since we are stroing the mdf file in an hadnler called 'mdf' in order to obtain the any signal data we do - 
    mdf.get('Signal_Name')

    This block is used to initalize the log mentioned in the path.

    additonal_channel_req : here we give the name of the channel whose data we would like to acquire as well, in form of a list.
    '''

    with MDF(path) as mdf:
        log_data = []
        log_data_trimmed = []
        failures = {"cur_failures": [], "fin_failures": [], "size": 0}
        DAS_control_functions = []
        # converting all control functions to lower - 
        lower_DMD_control_functions = [i.lower() for i in DMD_control_functions]
        DAS_log_warning_lamps = []
        DAS_log_additional_req_channels = []
        
        # mapping the warning lamps - 
        #wl_check_flag, mapped_wl = wl_mapper_DMD_to_DAS(DMD_warning_lamps)
        
        # if wl_check_flag == False:
        #     print_(f"{gen(f">>> ", "bold #FDCE01")}WL length do no match while mapping process 😟!")
        # else:
        #     print_(f"\n{gen(f">>> ", "bold #FDCE01")}WL data correctly mapped!")


        for channel in mdf.iter_channels():
            # log_data.append(channel)  # Store full channel
            # log_data_trimmed.append({
            #     'name': channel.name,
            #     'timestamps': channel.timestamps,
            #     'samples': channel.samples,
            #     'unit': channel.unit,
            #     'plot': channel.plot
            # })
            lower_channel_name = channel.name.lower()
            try: 
            # Storing current failures
                if channel.name.startswith("Fbd_cur"):
                    failures['cur_failures'].append(
                    {
                    'name': channel.name,
                    'timestamps': channel.timestamps,
                    'samples': channel.samples,
                    'unit': channel.unit,
                    'plot': channel.plot,
                    'transition_data':capture_transitions(channel)
                    })
                
                # Storing final failures
                elif channel.name.startswith("Fbd_fin"):
                    failures['fin_failures'].append(
                    {
                    'name': channel.name,
                    'timestamps': channel.timestamps,
                    'samples': channel.samples,
                    'unit': channel.unit,
                    'plot': channel.plot,
                    'transition_data':capture_transitions(channel)
                    })
                
                # storing control functions
                elif lower_channel_name.startswith("fsf_"): #and lower_channel_name in lower_DMD_control_functions:
                    if lower_channel_name in lower_DMD_control_functions:
                        DAS_control_functions.append(
                        {
                        'name': channel.name.lower(),
                        'timestamps': channel.timestamps,
                        'samples': channel.samples,
                        'unit': channel.unit,
                        'plot': channel.plot,
                        'transition_data':capture_transitions(channel)
                        })
                    if lower_channel_name.startswith('fsf_avh.') and 'fsf_avh' in lower_DMD_control_functions:
                        DAS_control_functions.append(
                        {
                        'name': 'fsf_avh',
                        'timestamps': channel.timestamps,
                        'samples': channel.samples,
                        'unit': channel.unit,
                        'plot': channel.plot,
                        'transition_data':capture_transitions(channel)
                        })
                    
                # store the WL data
                elif lower_channel_name.startswith('chn_') and lower_channel_name in mapped_wl:
                    DAS_log_warning_lamps.append(
                    {
                    'name': lower_channel_name,
                    'timestamps': channel.timestamps,
                    'samples': channel.samples,
                    'unit': channel.unit,
                    'plot': channel.plot,
                    'transition_data':capture_transitions(channel)
                    })


                    
                
                # storing the additional channels for analysis purpose
                elif channel.name in additonal_channel_req:
                    DAS_log_additional_req_channels.append(
                    {
                    'name': channel.name,
                    'timestamps': channel.timestamps,
                    'samples': channel.samples,
                    'unit': channel.unit,
                    'plot': channel.plot,
                    'transition_data':capture_transitions(channel)
                    })


                
                else: pass


                    
                

            except Exception as e: 
                print_(f"Error - {gen(str(e), 'bold #FE0202')}, occured while reading the channels from DAS log")

        failures["size"] = len(failures['cur_failures'])

        return (log_data, log_data_trimmed, failures, DAS_control_functions, DAS_log_warning_lamps, DAS_log_additional_req_channels)
            
#---------------------------------------------------------------------------------------------------------------------------------------
    # in order to plot it, we need to use the function as - log_data_tirmmed[46]['plot']()

def check_IGN_switch(ign_channel : dict, marker):
    """Checks if the IGN switch was toggled & if yes returns the indices of time stamps at which the IGN toggled happened"""
    data = ign_channel['transition_data'] # (transition_indices, transition_flag, constant_value)
    data_samples = ign_channel['samples']
    ign_indices = generate_sample_dict(data_samples)

    if data[1] == False:
        print_(f"\n{marker}{gen(f"IGN_Switch", "bold #FE9900")} was not toggled. Constant value - {data[2]}")
        return ign_indices
    else:
        print_(f"\n{marker}{gen(f"IGN_Switch", "bold #FE9900")} was toggled at points : {data[0]}")
        return ign_indices

#---------------------------------------------------------------------------------------------------------------------------------------
def system_state_check(SR_StateCurrent_channel : dict, marker):
    """Checks if the SR_StateCurrent was changed & if yes returns the indices of time stamps at which the IGN toggled happened
    returns - SR_state_cur_indices = {3: [indices], 2: [indices]...so on}
    """
    data = SR_StateCurrent_channel['transition_data'] # (transition_indices, transition_flag, constant_value)
    data_samples = SR_StateCurrent_channel['samples']
    SR_state_cur_indices = generate_sample_dict(data_samples)

    if len(SR_state_cur_indices) == 1:
        print_(f"\n{marker}{gen(f"System state", "bold #50E237")} was not changed at all.Constant value - {data[2]}")
        return SR_state_cur_indices
    else:
        print_(f"\n{marker}{gen(f"IGN_Switch", "bold #50E237")} was toggled at indice points : {data[0]}")
        return SR_state_cur_indices

#---------------------------------------------------------------------------------------------------------------------------------------

def plot_chosen_failure(chosen_failure : dict, cursor : int):
    """
    Helps to plot the chosen failure & the cursor at time where the degradation is taken.
    Note : cursor is the index at which we are taking the failure degradations.
    """

    samples = chosen_failure['samples']
    time_stamps = chosen_failure['timestamps']
    name = chosen_failure['name'][8:]

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(time_stamps, samples, label=name, marker='o')

    # Plot vertical line at the cursor index
    cursor_time = time_stamps[cursor]  # Get the time corresponding to the cursor
    plt.axvline(x=cursor_time, color='red', linestyle='--', label=f"Cursor at index {cursor}")

    # Labels and legend
    plt.xlabel("Time")
    plt.ylabel("Samples")
    plt.title(f"{name} with Cursor\n", fontsize=18, fontweight='bold', fontstyle='italic', family='Georgia')
    plt.legend()
    plt.grid()

    # Show plot
    plt.show()



#---------------------------------------------------------------------------------------------------------------------------------------
    # in order to plot it, we need to use the function as - log_data_tirmmed[46]['plot']()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    path = das_log_path_fetch()
    # Initialization
    log_data, log_data_trimmed, failures = initialize(path)

    # # fetching the cur & final failures that are set.
    cur_failures = find_set_cur_failures(failures['cur_failures'])
    fin_failures = find_set_fin_failures(failures['fin_failures'])

    #printing the results
    print_(gen('\n'+" RESULT ".center(99, '*')+"\n", 'bold yellow'))

    print("\nCur_failuers set - \n")
    if len(cur_failures) == 0:
        print_(f"{gen("No current failures set!\nLucky you, seems like the system is failure free!", "bold #00ff00")}")
    else:
        for i in cur_failures:
            print_(f"[bold #ff471a]{i[1]}[/bold #ff471a]")

    print_(gen('\n'+" ".center(99, '-')+"\n", 'green'))

    print("\nFin_failuers set - \n")
    if len(fin_failures) == 0:
        print_(f"{gen("No final failures set!", "bold #00ff00")}")
    else:
        for i in fin_failures:
            print_(f"[bold #ff471a]{i[1]}[/bold #ff471a]")
    print_(gen('\n'+" END ".center(99, '*')+"\n", 'bold yellow'))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def continue_prompt() -> bool:
    """Prompt the user to continue running the main function."""
    try:
        user_input = input("\nType 'yes' or 'y' to repeat execution: ").strip().lower() 
        return user_input in ('yes', 'y', '', ' ')
    except Exception as e:
            print_(gen(f"Error {str(e)} occurred while fetching prompt :(", 'bold #ff471a'))

# Main execution loop with error handling
def run_program():
    show_banner()
    while True:
        try:
            start = time.time()
            main()
            stop = time.time()
            t = round(stop-start, 2)
            print_(f"\nThat took {gen(str(t), "bold purple")}s....next version will be time optimised :)\n")
        except Exception as e:
            print_(gen(f"Error occurred during execution: {str(e)}", 'bold #ff471a'))
        if not continue_prompt():
            break
    print_(gen("\nExiting program...\n", "bold #ff6347"))

# Run the program
if __name__ == "__main__":
    run_program()
    
    







