<template>
  <v-container id="welcome" fluid fill-height style="max-height: 100vh;">
    <v-layout justify-center align-center column pa-5>
      <div
        id="content"
        class="display-2
          font-weight-black
          white--text
          text-xs-center
          mb-3"
      >
        AQUARIUM MANAGEMENT SYSTEM
      </div>
      <div
        id="content"
        class="headline
          font-weight-bold
          white--text
          text-xs-center"
      >
        The all-in-one solution for remote aquarium management.
      </div>
      <v-snackbar
        v-model="snackbar"
        :timeout="timeout"
      >
        Login session timed out!
        <v-btn
          color="blue"
          text
          @click="this.closeSessionTimeout"
        >
          Close
        </v-btn>
      </v-snackbar>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'welcome',
  data() {
    return {
      snackbar: false,
      timeout: 2000,
    }
  },
  computed: {
    ...mapState([
      'sessionTimeout',
    ]),
  },
  methods: {
    ...mapActions([
      'closeSessionTimeout',
    ]),
  },
};
</script>

<style scoped>
#welcome {
    background-image: url('../../public/koi-background.jpg');
    background-size: cover;
    width: 100%;
    height: 100%;
}
#content {
    text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
}
</style>
