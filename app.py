from src.blood_sample import BloodSample


def run():
    number_of_sample = input('Enter the no. of rows of blood sample tray:')
    if not number_of_sample.isdigit():
        print('Invalid Input')

    samples = _input_samples(number_of_sample)
    _print_samples(samples)


def _print_samples(samples):
    print('Results:\n')
    i = 1
    for sample in samples:
        print(f'Row {i}: {sample.number_of_matched} {sample.list_of_matched}')
        i += 1


def _input_samples(number_of_sample):
    samples = []
    print('Enter the results of the covid blood samples:\n')
    for i in range(int(number_of_sample)):
        sample_input = input()
        sample = BloodSample(sample_input)
        if not sample.is_valid():
            print('Invalid Input')
        else:
            sample.parse()
            samples.append(sample)
    return samples


if __name__ == '__main__':
    run()
