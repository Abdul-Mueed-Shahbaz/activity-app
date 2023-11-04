<template>
  <div class="dialog">
    <div class="dialog-content">
      <h2>Create a New Item</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="formName" required />
        </div>

        <div class="form-group">
          <label for="description">Description:</label>
          <textarea id="description" v-model="formDescription"></textarea>
        </div>
        <button type="submit" class="submit-button">Submit</button>
        <button @click="$emit('close')" class="close-button">Close</button>
      </form>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import { useStore } from "vuex";

export default defineComponent({
  emits: ["close", "onFormSubmit"],
  setup(_, { emit }) {
    const store = useStore();

    const formName = computed({
      get() {
        return store.getters["activity/getFormName"];
      },
      set(val) {
        store.dispatch("activity/updateFormName", val);
      },
    });

    const formDescription = computed({
      get() {
        return store.getters["activity/getFormDescription"];
      },
      set(val) {
        store.dispatch("activity/updateFormDescription", val);
      },
    });

    function resetForm() {
      formName.value = "";
      formDescription.value = "";
    }
    function handleSubmission() {
      resetForm();
      emit("onFormSubmit");
    }
    function submitForm() {
      store
        .dispatch("activity/createActivty", {
          name: formName.value,
          desc: formDescription.value,
        })
        .then(() => {
          handleSubmission();
        });
    }
    return {
      formName,
      formDescription,
      submitForm,
      // Other variables and methods
    };
  },
});
</script>

<style scoped>
.dialog {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog-content {
  background: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 800px;
}
.error-message {
  color: #ff2600;
  font-size: 14px;
  margin-top: 5px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
}

input,
textarea {
  width: 80%;
  padding: 10px;
  border: 1px solid #aaaaaa;
  border-radius: 5px;
  font-size: 16px;
  outline: none;
}

textarea {
  height: 100px;
}

.submit-button,
.close-button {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-right: 10px;
}

.close-button {
  background-color: #ff6347;
}

.submit-button:hover,
.close-button:hover {
  background-color: #0056b3;
}

.submit-button:focus,
.close-button:focus {
  outline: none;
}
</style>
