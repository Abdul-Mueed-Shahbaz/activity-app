<template>
  <div style="display: flex; justify-content: center">
    <table id="activites" class="activites">
      <thead>
        <tr>
          <th>ID</th>
          <th>Created On</th>
          <th>Updated On</th>
          <th>Completed</th>
          <th>Name</th>
          <th>Description</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(activity, index) in activities" :key="activity.id">
          <td>{{ activity.id }}</td>
          <td>{{ activity.created_on }}</td>
          <td>{{ activity.updated_on }}</td>
          <td>
            <input
              type="checkbox"
              :checked="activity.completed"
              @input="
                (ev) =>
                  $emit('changeStatus', {
                    value: ev.target.checked,
                    activityId: activity.id,
                    index,
                  })
              "
            />
          </td>
          <td>{{ activity.name }}</td>
          <td>{{ activity.desc || "N/A" }}</td>
          <td>
            <button @click="$emit('delete', activity.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    activities: {
      type: Object,
      required: true,
    },
  },
  emits: ["delete", "changeStatus"],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
$breakpoint-alpha: 480px;
.activites {
  background: #34495e;
  color: #fff;
  border-radius: 0.4em;
  overflow: hidden;
  tr {
    border-color: lighten(#34495e, 10%);
  }
  th,
  td {
    margin: 0.5em 1em;
    @media (min-width: $breakpoint-alpha) {
      padding: 1em !important;
    }
  }
  th,
  td:before {
    color: #dd5;
  }
}
</style>
