// import { useState } from "react";

import { useEffect } from "react";
import "./App.css";
import { useCounterStore } from "./store";


// This shows "vanilla" access to Zustand outside React render flow (Last Thing To Explain).
// `getState()` reads the latest snapshot without subscribing the component.
// const logCount = () => {
//   const count = useCounterStore.getState().count;
//   return console.log(count);
// };


// `setState` can update Zustand directly from any function.
// Useful for demos, scripts, or non-React event sources.
const setLogCount = () => {
  useCounterStore.setState({ count: 1 });
};

function App() {
  
  // Local React state version (kept for comparison with global Zustand state).
  // const [count] = useState(0);

  
  // Selector subscribes this component only to `count` updates.
  const count = useCounterStore((state) => state.count);

  return <OtherComponent count={count} />;
}

const OtherComponent = ({ count }: { count: number }) => {
  
  // Sync increment action (kept for comparison with async action below).
  // const increment = useCounterStore((state) => state.increment);

  
  // Async action from the store; demonstrates that Zustand actions can await.
  const incrementAsync = useCounterStore((state) => state.incrementAsync);

  
  // Another action subscription; component re-renders only if this selector changes.
  const decrement = useCounterStore((state) => state.decrement);

  
  // Example side effect: read current state once on mount with `getState()`.
  // useEffect(() => {
  //   logCount();
  // }, []);

  
  // Example side effect: force-write to store on mount using `setState`.
  useEffect(() => {
    setLogCount()
  },[])

  return (
    <div>
      {/* Teaching note: Sync increment button (disabled for now). */}
      {/* <button onClick={increment}>Increment</button> */}

      {/* Teaching note: Active button calls async store action. */}
      {/* <button onClick={increment}>Increment</button> */}
      <button onClick={incrementAsync}>Increment</button>

      {/* Teaching note: Value is passed as prop from App, sourced from Zustand. */}
      <div>{count}</div>

      {/* Teaching note: Decrement uses another store action. */}
      <button onClick={decrement}>Decrement</button>

      {/* Teaching note: Optional button to print store state to console. */}
      {/* <button onClick={logCount}>Log Count</button> */}
    </div>
  );
};

export default App;
