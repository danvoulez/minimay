<script>
  import LogLineView from '../components/LogLineView.svelte';
  import CommunicatorView from '../components/CommunicatorView.svelte';
  import ContracterView from '../components/ContracterView.svelte';
  import RightMenu from '../components/RightMenu.svelte';
  import LeftMenu from '../components/LeftMenu.svelte';

  let mode = 'logline';
  let fields = null;

  function setMode(m) {
    mode = m;
  }

  function onRegistered(e) {
    fields = e.detail.fields;
  }
</script>

<div class="layout">
  <LeftMenu {mode} {setMode} />
  <div class="content">
    {#if mode === 'logline'}
      <LogLineView on:registered={onRegistered} />
    {:else if mode === 'communicator'}
      <CommunicatorView />
    {:else}
      <ContracterView />
    {/if}
  </div>
  <RightMenu {fields} />
</div>

<style>
  .layout {
    display: flex;
    height: 100vh;
  }
  .content {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
