import { createStore } from "vuex";
import activity from "./activity";
import createPersistedState from "vuex-persistedstate";

const Store = createStore({
  modules: {
    activity,
  },
  plugins: [
    createPersistedState({
      paths: ["activity"],
    }),
  ],
  // enable strict mode (adds overhead!)
  // for dev mode and --debug builds only
  strict: process.env.DEBUGGING,
});

export default Store;
