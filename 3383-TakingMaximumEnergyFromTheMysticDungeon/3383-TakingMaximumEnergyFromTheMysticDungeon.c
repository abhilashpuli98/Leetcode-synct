// Last updated: 2/5/2026, 7:39:51 AM
int maximumEnergy(int* energy, int energySize, int k) {
    int maxEnergy = INT_MIN;
    int energySequence[energySize];

    for (int x = energySize-1; x >= 0; x--) {
        int nextEnergy = (x + k < energySize) ? energySequence[x + k] : 0;
        energySequence[x] = energy[x] + nextEnergy;
        if (energySequence[x] > maxEnergy)
            maxEnergy = energySequence[x];
    }
    return maxEnergy;
}