<script>
  import { selectedLog } from './stores.js';
  import { onMount } from 'svelte';
  let timeline = [];
  onMount(async () => {
    const res = await fetch('/timeline');
    if(res.ok) timeline = await res.json();
  });
</script>

<div>
  {#if $selectedLog}
    <h3>Detalhes</h3>
    <pre>{JSON.stringify($selectedLog, null, 2)}</pre>
  {/if}
  {#if timeline.length}
    <h3>Timeline</h3>
    <ul>
      {#each timeline as item}
        <li>{item.who}: {item.did} {item.this}</li>
      {/each}
    </ul>
  {/if}
</div>

<style>
  div { font-size: 0.9rem; }
  pre { white-space: pre-wrap; word-break: break-all; }
  ul { padding-left: 1rem; }
</style>
