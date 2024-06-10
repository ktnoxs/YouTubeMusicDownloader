

def get_available_core(working_core_count, cpu_count, queue_count=0):
    available_core_count = min(working_core_count, cpu_count)

    if queue_count < available_core_count:
        available_core_count = queue_count

    return available_core_count
