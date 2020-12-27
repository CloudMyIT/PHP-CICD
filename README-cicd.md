# Using Environment During Development

(This can be packaged for your individual needs)

Because this setup runs against multiple different possible environment setups, its best to put all of your tests into a single file to run.

> Builds will Pass/Fail no CI details about what server version combinations failed, or what exact test failed.

1) Update "CI_COMMAND" in `settings.py` to run the command that will launch all of your tests.

2) Configure your CI to launch in a "privilaged" docker container that has python3

3) Configure your CI to run the `ci.py` command.

4) Profit.