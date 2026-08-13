import { create } from "zustand";

// This type defines the store shape: state fields + action functions.
type CounterStore = {
  count: number;
  increment: () => void;
  decrement: () => void;
  incrementAsync: () => Promise<void>;
};



// export const useLoginStore = create<

// `create` builds a hook (`useCounterStore`) that components use to read state/actions.
// `set` is the updater function provided by Zustand.
export const useCounterStore = create<CounterStore>((set) => ({
  count: 0,

  // Sync action: update based on previous state for safe increments.
  increment: () => {
    // Direct assignment example (overwrites count to fixed value).
    // set({ count: 1 });

    // Functional updater reads previous state and derives next state.
    // set((state) => ({ count: state.count + 1 }));
  },

  // Async action: wait, then update state the same way as sync actions.
  incrementAsync: async () => {
    await new Promise((resolve) => setTimeout(resolve, 1000));
    set((state) => ({ count: state.count + 1 }));
  },


  // Decrement mirrors increment but subtracts from previous state.
  decrement: () => {
    // Direct assignment example (forces a fixed negative value).
    // set({count: -1})
    set((state) => ({ count: state.count - 1 }));
  },
}));
